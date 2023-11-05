import warnings

from app.db.firebase import users_collection
from app.models.user import UserPrivateModel, UserModel
from app.enums.user import UserAuthType, UserRole
from app.utils import generate_timestamp, generate_unique_id, hash_password
from app.utils.firebase import convert_doc_refs
from app.constants import filter_warning_message

class UserService:

    def get_all():
        users = users_collection.stream()
        # Convert each DocumentSnapshot to a dictionary and add it to a list
        user_list = [user.to_dict() for user in users]
        user_list_doc_refs = convert_doc_refs(user_list)
        return user_list_doc_refs

    def get(id):
        warnings.filterwarnings(
            "ignore", 
            category = UserWarning, 
            message = filter_warning_message
        )
        # Query the collection where 'id' is equal to user_id
        users = users_collection.where('id', '==', id).limit(1).stream()

        # Users is an iterator of DocumentSnapshot
        # Converting DocumentSnapshot to a dictionary

        user_list = [user.to_dict() for user in users]
        # NOTE: collection_ref.where returns an array of documents.
        # We only want the first document in the array.
        user = user_list[0] if user_list else None
        return user
        # return users_collection.document(id).get().to_dict()
    
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

        user_model = UserModel(**user_data)
        user_private_model = UserPrivateModel(
            **user_model.dict(),
            password = user_data["password"]
        )

        # Add the user to the 'users' collection
        user_ref = users_collection.document(user_private_model.id)
        user_ref.set(user_private_model.dict())
        return user_ref
    
    # NOTE: data argument should only contain name and email.
    # TODO: Need to figure out a way to validate that data only can contain those 2 fields.
    def update(id, data):
        update_data = {
            **data,
            'updated_at': generate_timestamp()
        }
        users_ref = users_collection.document(id)
        users_ref.update(update_data)
        return data
    
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
        return id
    
    def activate(id):
        user_ref = users_collection.document(id)
        user_ref.update({
            'active': True,
            'update_at': generate_timestamp()
        })
        return id