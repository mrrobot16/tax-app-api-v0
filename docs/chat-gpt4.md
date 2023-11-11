Ok Perkins, i am trying to test an endpoint takes several arguments 
that happen to be models which have fields that if not included it will have default values.

Now my endpoint takes 3 arguments the first 2 are type Models/BaseModels, the third one is a Background Tasks. 


Is it possible that my request can have just the fields necessary like in this example



my models
````
from pydantic import BaseModel
from datetime import datetime

from app.models.message import MessageGroupModel, MessageModel
from app.utils import generate_timestamp, generate_unique_id

class ConversationModel(BaseModel):
    id: str = generate_unique_id()
    user_id: str
    name: str
    messages: list[MessageModel] = []
    message_groups: list[MessageGroupModel] = []
    active: bool = True
    created_at: datetime = generate_timestamp()
    updated_at: datetime = generate_timestamp()

    def add_message(self, message: MessageModel):
        self.messages.append(message)
        self.updated_at = generate_timestamp()
    
    def add_message_group(self, message_group: MessageGroupModel):
        self.message_groups.append(message_group)
        self.updated_at = generate_timestamp()

        from pydantic import BaseModel, Field
        from datetime import datetime
        from typing import Optional
        
        
        from app.enums.user import UserRole
        from app.utils import generate_timestamp, generate_unique_id
        
        class MessageModel(BaseModel):
            id: str = generate_unique_id()
            user_id: str
            conversation_id: str
            content: str
            role: UserRole = Field(default = 'user', alias = 'role')
            created_at: datetime = generate_timestamp()
            updated_at: datetime = generate_timestamp()
            class Config:
                use_enum_values = True
                populate_by_name = True
````

my endpoint
````
@conversations_controller.post("/new/message/chat-completion")
def new_conversation_chat_completion_message(conversation: ConversationModel, message: MessageModel, tasks: BackgroundTasks):
    chat_completion_response = ConversationService().new_conversation_chat_completion_message(conversation, message, tasks)
    return chat_completion_response
````

My request
````
{
    "conversation": { 
        "id": "50fe00ca-7d2c-4c61-8", 
        "user_id": "60fbe8cc-a9dc-4ec4-a", 
        "name": "Test Conversation id: 50fe00ca-7d2c-4c61-8", 
        "messages": [], "active": True
    }, 
    "message": {
        "content": "Perkins, what is a 1120?", "role": "user"
    }
}
````

my test 
````

def test_new_conversation_chat_completion_message():
    json = {
        "conversation": { 
            "id": "50fe00ca-7d2c-4c61-8", 
            "user_id": "60fbe8cc-a9dc-4ec4-a", 
            "name": "Test Conversation id: 50fe00ca-7d2c-4c61-8", 
            "messages": [], "active": True
        }, 
        "message": {
            "content": "Perkins, what is a 1120?", "role": "user"
        }
    }
    response = client.post("/conversations/new/message/chat-completion", json = json)
    assert response.status_code == 200
````

My error
````

================================================================================================= FAILURES =================================================================================================
______________________________________________________________________________ test_new_conversation_chat_completion_message _______________________________________________________________________________

    def test_new_conversation_chat_completion_message():
        json = {
            "conversation": conversation_data,
            "message": user_message,
        }
        print('\n')
        print(str(json))
        response = client.post("/conversations/new/message/chat-completion", json = json)
>       assert response.status_code == 200
E       assert 422 == 200
E        +  where 422 = <Response [422 Unprocessable Entity]>.status_code

tests/integrations/controllers/test_conversation.py:66: AssertionError
========================================================================================= short test summary info ==========================================================================================
FAILED tests/integrations/controllers/test_conversation.py::test_new_conversation_chat_completion_message - assert 422 == 200


````