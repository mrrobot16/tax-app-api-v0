import random

from app.enums.user import UserRole

user_role_messages = [
    {
        "content": "Perkins, what is a 1040?",
        "role": UserRole.USER.value,
    },
    {
        "content": "Perkins, what is a 1120?",
        "role": UserRole.USER.value,
    },
    {
        "content": "Perkins, what is a 1099-NEC?",
        "role": UserRole.USER.value,
    },
    {
        "content": "Perkins, what is a Schedule C?",
        "role": UserRole.USER.value,
    },
    {
        "content": "Perkins, what is a 1099-INT?",
        "role": UserRole.USER.value,
    }
]

assistant_role_messages = [
    {
        "content": "1040 for is for individual tax returns",
        "role": UserRole.ASSISTANT,
    },
    {
        "content": "1120 for is for s-corporation tax returns",
        "role": UserRole.ASSISTANT,
    },
    {
        "content": "1099-NEC is to report nonemployee compensation",
        "role": UserRole.ASSISTANT,
    },
    {
        "content": "Schedule C to report income or (loss) from a business you operated or a profession you practiced as a sole proprietor",
        "role": UserRole.ASSISTANT,
    },
    {
        "content": "1099-INT to report interest income received",
        "role": UserRole.ASSISTANT,
    }
]

# NOTE: Need to generate a random number from 0 to the length of 
# the messages_user_role and messages_asssistant_role array that need to be the same.

random_number = random.randint(0, len(user_role_messages) - 1)

user_message = user_role_messages[random_number]
assistant_message = assistant_role_messages[random_number]

message_group = [
    user_message,
    assistant_message
]
