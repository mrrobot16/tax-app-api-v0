from app.db.firebase import users_collection
from app.enums.user import UserAuthType, UserRole
from app.utils import generate_timestamp, generate_unique_id, hash_password
from app.utils.firebase import convert_doc_refs

class UserService:

    def get_all():
        users = users_collection.stream()
        # Convert each DocumentSnapshot to a dictionary and add it to a list
        user_list = [user.to_dict() for user in users]
        user_list_doc_refs = convert_doc_refs(user_list)
        return user_list_doc_refs

    def get(id):
        # Query the collection where 'id' is equal to user_id
        users = users_collection.where('id', '==', id).limit(1).stream()

        # Users is an iterator of DocumentSnapshot
        # Converting DocumentSnapshot to a dictionary

        user_list = [user.to_dict() for user in users]
        # NOTE: collection_ref.where returns an array of documents.
        # We only want the first document in the array.
        user = user_list[0] if user_list else None
        user_doc_ref = convert_doc_refs(user)
        return user_doc_ref
    
    def new(
            name = "test_name",
            email = "test@email.com", 
            password = "test_password", 
            role = UserRole.USER.value, 
            conversations = [], 
            auth_type = UserAuthType.EMAIL_PASSWORD.value,
        ):
        id = generate_unique_id()  # Generate a unique 20-character ID
        hashed_password = str(hash_password(password))  # This is a placeholder for now.
        created_at = generate_timestamp()  # Get current timestamp
        updated_at = created_at

        user_data = {
            'id': id,
            'name': name,
            'email': email,
            'password': hashed_password,
            'conversations': conversations,
            'active': True,
            'role': role,
            'auth_type': auth_type,
            'created_at': created_at,
            'updated_at': updated_at
        }

        user_ref = users_collection.document(user_data["id"])
        user_ref.set(user_data)
        # return user_data
        # After setting the data, get the document back as a snapshot and convert it to a dictionary
        user_snapshot = user_ref.get()
        if user_snapshot.exists:
            return user_snapshot.to_dict()
        else:
            return None

    # NOTE: Need to figure out a way to validate that data argument 
    # can only contain name and email.
    def update(id, data):
        update_data = {
            **data,
            'updated_at': generate_timestamp()
        }
        user_ref = users_collection.document(id)
        user_ref.update(update_data)

        # Now read the updated document
        updated_document = user_ref.get()
        if updated_document.exists:
            user_doc_ref = convert_doc_refs(updated_document.to_dict())
            return user_doc_ref
        else:
            # Handle the case where the document does not exist
            return None
    
    def delete(id):
        users_ref = users_collection.document(id)
        users_ref.delete()
        return id
    
    def deactivate(id):
        user_ref = users_collection.document(id)
        user_ref.update({
            'active': False,
            'update_at': generate_timestamp()
        })
        # Retrieve the updated document
        user_doc = user_ref.get()
        # Return the document data as a dictionary
        return user_doc.to_dict()
    
    def activate(id):
        user_ref = users_collection.document(id)
        user_ref.update({
            'active': True,
            'update_at': generate_timestamp()
        })
        # Retrieve the updated document
        user_doc = user_ref.get()
        # Return the document data as a dictionary
        return user_doc.to_dict()