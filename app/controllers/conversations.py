from typing import Dict, Optional
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.services.conversation import ConversationService
from app.models.conversation import ConversationModel

conversations_controller = APIRouter()

@conversations_controller.get("/status")
def conversation_status():
    return JSONResponse(content = {"status": status.HTTP_200_OK, })

@conversations_controller.get("/")
def get_all_conversations():
    conversations = ConversationService.get_all()
    return conversations

@conversations_controller.get("/{id}")
def get_conversation(id: str):
    conversation = ConversationService.get(id)
    return conversation

@conversations_controller.post("/new")
def new_conversation(conversation: ConversationModel):
    conversation_data = {
        "name": conversation.conversation
    }
    conversation = ConversationService.new(**conversation_data)
    return conversation

@conversations_controller.put("/{id}")
def update_conversation(id: str, data: Dict[str, Optional[str]]):
    # Validate that data only contains 'email' and 'name' keys are provided
    for key in data:
        if key not in ["name"]:
            raise HTTPException(status_code=400, detail=f"Invalid field: {key}")
    conversation = ConversationService.update(id, data)
    return conversation

# @conversations_controller.delete("/{id}")
# def delete_conversation(id: str):
#     conversation = ConversationService.delete(id)
#     return JSONResponse(content = conversation)

@conversations_controller.put("/deactivate/{id}")
def deactivate_conversation(id: str):
    conversation = ConversationService.deactivate(id)
    return conversation

@conversations_controller.put("/activate/{id}")
def activate_conversation(id: str):
    conversation = ConversationService.activate(id)
    return conversation
