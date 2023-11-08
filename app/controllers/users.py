from typing import Dict, Optional
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse


from app.models.user import UserModel, UserPrivateModel
from app.services.user import UserService

user_controller = APIRouter()

@user_controller.get("/status")
def user_status():
    return JSONResponse(content = {"status": status.HTTP_200_OK, })

@user_controller.get("/all")
def get_all_users():
    users = UserService.get_all()
    return users

@user_controller.get("/{id}")
def get_user(id: str):
    user = UserService.get(id)
    return user

@user_controller.post("/new")
def new_user(user: UserPrivateModel):
    user_data = {
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "auth_type": user.auth_type,
    }
    user = UserService.new(**user_data)
    return user

@user_controller.put("/{id}")
def update_user(id: str, data: Dict[str, Optional[str]]):
    # Validate that data only contains 'email' and 'name' keys are provided
    for key in data:
        if key not in ["email", "name"]:
            raise HTTPException(status_code=400, detail=f"Invalid field: {key}")
    user = UserService.update(id, data)
    return user

# @user_controller.delete("/{id}")
# def delete_user(id: str):
#     user = UserService.delete(id)
#     return JSONResponse(content = user)

@user_controller.put("/deactivate/{id}")
def deactivate_user(id: str):
    user = UserService.deactivate(id)
    return user

@user_controller.put("/activate/{id}")
def activate_user(id: str):
    user = UserService.activate(id)
    return user
