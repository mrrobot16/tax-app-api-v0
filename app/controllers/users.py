from typing import Dict, Optional
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse


from models.user import UserModel, UserPrivateModel
from services.user import UserService

users_controller = APIRouter()

@users_controller.get("/status")
def user_status():
    return JSONResponse(content = {"status": status.HTTP_200_OK, })

@users_controller.get("/")
def get_users():
    users = UserService.get_all()
    return users

@users_controller.get("/{id}")
def get_user(id: str):
    user = UserService.get(id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@users_controller.post("/new", response_model = UserModel)
def new_user(user: UserPrivateModel) -> UserModel:
    user_data = {
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "auth_type": user.auth_type,
    }
    user = UserService.new(**user_data)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest user login failed, try")
    return user

@users_controller.put("/{id}")
def update_user(id: str, data: Dict[str, Optional[str]]):
    # Validate that data only contains 'email' and 'name' keys are provided
    for key in data:
        if key not in ["email", "name"]:
            raise HTTPException(status_code=400, detail=f"Invalid field: {key}")
    user = UserService.update(id, data)
    return user

# @users_controller.delete("/{id}")
# def delete_user(id: str):
#     user = UserService.delete(id)
#     return JSONResponse(content = user)

@users_controller.put("/deactivate/{id}")
def deactivate_user(id: str):
    user = UserService.deactivate(id)
    return user

@users_controller.put("/activate/{id}")
def activate_user(id: str):
    user = UserService.activate(id)
    return user
