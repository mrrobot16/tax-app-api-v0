from app.db.firebase import conversations_collection, firestore, users_collection
from app.models.conversation import ConversationModel
from app.models.message import MessageModel
from app.utils import generate_timestamp
from app.utils.firebase import convert_doc_refs

class ConversationService:

    def get_all():
        conversations = conversations_collection.stream()
        # Convert each DocumentSnapshot to a dictionary and add it to a list
        conversations_list = [conversation.to_dict() for conversation in conversations]
        conversations_list_doc_refs = convert_doc_refs(conversations_list)
        return conversations_list_doc_refs

    def get(id):
        # Query the collection where 'id' is equal to user_id
        conversations = conversations_collection.where('id', '==', id).limit(1).stream()

        # Conversations is an iterator of DocumentSnapshot
        # Converting DocumentSnapshot to a dictionary

        conversations_list = [conversation.to_dict() for conversation in conversations]
        # NOTE: collection_ref.where returns an array of documents.
        # We only want the first document in the array.
        conversation = conversations_list[0] if conversations_list else None
        conversation_doc_ref = convert_doc_refs(conversation)
        return conversation_doc_ref
    
    def get_all_by_user(user_id):
        # Query the collection where 'user_id' is equal to user_id
        conversations = conversations_collection.where('user_id', '==', user_id).stream()

        # Conversations is an iterator of DocumentSnapshot
        # Converting DocumentSnapshot to a dictionary

        conversations_list = [conversation.to_dict() for conversation in conversations]
        # NOTE: collection_ref.where returns an array of documents.
        # We only want the first document in the array.
        conversation = conversations_list if conversations_list else None
        conversation_doc_ref = convert_doc_refs(conversation)
        return conversation_doc_ref
    
    def new(conversation: ConversationModel):
        conversation_ref = conversations_collection.document(conversation.id)
        conversation_ref.set(conversation.model_dump())

        user_ref = users_collection.document(conversation.user_id)
        user_ref.update({
            'conversations': firestore.ArrayUnion([conversation_ref])
        })

        # After setting the data, get the document back as a snapshot and convert it to a dictionary
        conversation_snapshot = conversation_ref.get()
        if conversation_snapshot.exists:
            return conversation_snapshot.to_dict()
        else:
            return None
        
    def new_message(message: MessageModel):
        conversation_ref = conversations_collection.document(message.conversation_id)
        try:
            conversation_ref.update({
                'updated_at': generate_timestamp(),
                'messages': firestore.ArrayUnion([message.model_dump()])
            })
            return message.model_dump()
        except Exception as error:
            print('error in services/conversation.py/new_message:', error)
            return error

    # NOTE: Need to figure out a way to validate that data argument 
    # can only contain name
    def update(id, data):
        update_data = {
            **data,
            'updated_at': generate_timestamp()
        }
        conversation_ref = conversations_collection.document(id)
        conversation_ref.update(update_data)

        # Now read the updated document
        updated_document = conversation_ref.get()
        if updated_document.exists:
            conversation_doc_ref = convert_doc_refs(updated_document.to_dict())
            return conversation_doc_ref
        else:
            # Handle the case where the document does not exist
            return None
    
    def delete(id):
        conversations_ref = conversations_collection.document(id)
        conversations_ref.delete()
        return id
    
    def deactivate(id):
        conversation_ref = conversations_collection.document(id)
        conversation_ref.update({
            'active': False,
            'updated_at': generate_timestamp()
        })
        # Retrieve the updated document
        conversation_doc = conversation_ref.get()
        conversation = conversation_doc.to_dict()
        # Return the document data as a dictionary
        return convert_doc_refs(conversation)
    
    def activate(id):
        conversation_ref = conversations_collection.document(id)
        conversation_ref.update({
            'active': True,
            'updated_at': generate_timestamp()
        })
        # Retrieve the updated document
        conversation_doc = conversation_ref.get()
        conversation = conversation_doc.to_dict()
        # Return the document data as a dictionary
        return convert_doc_refs(conversation)