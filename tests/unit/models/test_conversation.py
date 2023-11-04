import random
from app.models.conversation import ConversationModel
from app.models.message import MessageModel, MessageGroupModel
from app.utils import generate_timestamp, generate_unique_id

from tests.fixtures.user import user_data
from tests.fixtures.conversation import conversation_data
from tests.fixtures.message import assistant_role_messages, user_role_messages

random_number = random.randint(0, len(user_role_messages) - 1)
random_number_2 = random.randint(0, len(user_role_messages) - 1)

conversation = ConversationModel(
    **conversation_data, 
    created_at = generate_timestamp(), 
    updated_at = generate_timestamp()
)

def test_conversation_instanciated():
    # NOTE: Need to create assertion that ConversationModel instanciated correctly.
    assert conversation
    assert conversation.id == conversation_data["id"]
    assert conversation.user_id == user_data["id"]
    assert conversation.name == f'Test Conversation id: {conversation.id}'
    assert len(conversation.messages) == 0
    assert len(conversation.message_groups) == 0
    assert conversation.active == True
    assert conversation.created_at
    assert conversation.updated_at

def test_conversation_add_user_message():
    user_message = user_role_messages[random_number]
    message = MessageModel(
        **user_message, 
        user_id = conversation.user_id, 
        conversation_id = conversation.id,
        created_at = generate_timestamp()
    )
    conversation.add_message(message)
    assert conversation.messages
    assert len(conversation.messages) == 1
    assert conversation.messages[0].id == message.id
    assert conversation.messages[0].user_id == message.user_id
    assert conversation.messages[0].conversation_id == message.conversation_id

def test_conversation_add_assistant_message():
    assistant_message = assistant_role_messages[random_number]
    message = MessageModel(
        **assistant_message, 
        user_id = conversation.user_id, 
        conversation_id = conversation.id,
        created_at = generate_timestamp()
    )
    conversation.add_message(message)
    assert conversation.messages
    assert len(conversation.messages) == 2
    assert conversation.messages[1].id == message.id
    assert conversation.messages[1].user_id == message.user_id
    assert conversation.messages[1].conversation_id == message.conversation_id

def test_conversation_add_message_group():
    message_group = MessageGroupModel(
        id = generate_unique_id(), 
        user_id = conversation.user_id, 
        conversation_id = conversation.id,
        messages = conversation.messages[-2:]
    )
    conversation.add_message_group(message_group)
    assert conversation.message_groups
    assert len(conversation.message_groups) == 1
    assert len(conversation.message_groups[0].messages) == 2
    assert len(conversation.message_groups[0].messages) % 2 == 0
    assert conversation.message_groups[0].id == message_group.id
    assert conversation.message_groups[0].user_id == message_group.user_id
    assert conversation.message_groups[0].conversation_id == message_group.conversation_id
    assert conversation.message_groups[0].messages[0].id == conversation.messages[0].id
    assert conversation.messages[0].content == conversation.message_groups[0].messages[0].content

def test_conversation_add_user_message_2():
    user_message = user_role_messages[random_number_2]
    message = MessageModel(
        **user_message, 
        user_id = conversation.user_id, 
        conversation_id = conversation.id,
        created_at = generate_timestamp()
    )
    conversation.add_message(message)
    assert conversation.messages
    assert len(conversation.messages) == 3
    assert conversation.messages[2].id == message.id
    assert conversation.messages[2].user_id == message.user_id
    assert conversation.messages[2].conversation_id == message.conversation_id

def test_conversation_add_assistant_message_2():
    assistant_message = assistant_role_messages[random_number_2]
    message = MessageModel(
        **assistant_message, 
        user_id = conversation.user_id, 
        conversation_id = conversation.id,
        created_at = generate_timestamp()
    )
    conversation.add_message(message)
    assert conversation.messages
    assert len(conversation.messages) == 4
    assert conversation.messages[3].id == message.id
    assert conversation.messages[3].user_id == message.user_id
    assert conversation.messages[3].conversation_id == message.conversation_id

def test_conversation_add_message_group2():
    message_group = MessageGroupModel(
        id = generate_unique_id(), 
        user_id = conversation.user_id, 
        conversation_id = conversation.id,
        messages = conversation.messages[-2:]
    )
    conversation.add_message_group(message_group)
    assert conversation.message_groups
    assert len(conversation.message_groups) == 2
    assert len(conversation.message_groups[1].messages) == 2
    assert len(conversation.message_groups[1].messages) % 2 == 0
    assert conversation.message_groups[1].id == message_group.id
    assert conversation.message_groups[1].user_id == message_group.user_id
    assert conversation.message_groups[1].conversation_id == message_group.conversation_id
    assert conversation.messages[2].content == conversation.message_groups[1].messages[0].content