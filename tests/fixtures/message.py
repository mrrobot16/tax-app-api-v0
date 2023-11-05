import random
from app.utils import generate_unique_id, generate_timestamp
from app.enums.user import UserRole

user_role_messages = [
    {
        "id": generate_unique_id(),
        "content": "Perkins, what is a 1040?",
        "role": UserRole.USER,
    },
    {
        "id": generate_unique_id(),
        "content": "Perkins, what is a 1120?",
        "role": UserRole.USER,
    },
    {
        "id": generate_unique_id(),
        "content": "Perkins, what is a 1099-NEC?",
        "role": UserRole.USER,
    },
    {
        "id": generate_unique_id(),
        "content": "Perkins, what is a Schedule C?",
        "role": UserRole.USER,
    },
    {
        "id": generate_unique_id(),
        "content": "Perkins, what is a 1099-INT?",
        "role": UserRole.USER,
    }
]

assistant_role_messages = [
    {
        "id": generate_unique_id(),
        "content": "1040 for is for individual tax returns",
        "role": UserRole.ASSISTANT,
    },
    {
        "id": generate_unique_id(),
        "content": "1120 for is for s-corporation tax returns",
        "role": UserRole.ASSISTANT,
    },
    {
        "id": generate_unique_id(),
        "content": "1099-NEC is to report nonemployee compensation",
        "role": UserRole.ASSISTANT,
    },
    {
        "id": generate_unique_id(),
        "content": "Schedule C to report income or (loss) from a business you operated or a profession you practiced as a sole proprietor",
        "role": UserRole.ASSISTANT,
    },
    {
        "id": generate_unique_id(),
        "content": "1099-INT to report interest income received",
        "role": UserRole.ASSISTANT,
    }
]

# NOTE: Need to generate a random number from 0 to the length of 
# the messages_user_role and messages_asssistant_role array that need to be the same.

random_number = random.randint(0, len(user_role_messages) - 1)

user_message = user_role_messages[random_number]
# assistant_message = messages_assistant_role[random_number]
