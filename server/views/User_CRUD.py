from datetime import timedelta
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from server.database import *
from server.views.token import *
from server.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.accounts import (
    ErrorResponseModel,
    Login,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()
crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
def get_password_hash(password):
    return crypt_context.hash(password)
# For create
@router.post("/", response_description="user data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    if user["social"]==True:
        new_user = await add_user_by_social(user)
    else:
        user["passWords"]=get_password_hash(user["passWords"])
        new_user = await add_user(user)
    return {"code": 200,"User ID":new_user }

@router.post("/login/", response_description="user login ")
async def login(user: Login = Body(...)):
    user = jsonable_encoder(user)
    if user["social"]==True:
        users = await user_collection.find_one({"mobile": user['email']})
    
    try:
        int(user["email"])
        users = await user_collection.find_one({"mobile": user['email']})
    except:
        users = await user_collection.find_one({"email": user['email']})
        # mobiles = await user_collection.find_one({"mobile": user['email']})
    if users and user["social"]==True:
        access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer","flag":users['flag']}
    if users:
        if  (verify_password(user['passWords'],users['passWords'])):
            access_token = create_access_token(
            data={"sub": user["email"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
            return {"access_token": access_token, "token_type": "bearer","flag":users['flag']}
        else:
            return {"code": 200,"message":"Password not match" }
    return {"code": 200,"message":"User not found invalid email" }

# For read
@router.get("/", response_description="users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

#userdata get by id
@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")

# retrieve_user_by_name
@router.get("/name/{name}", response_description="user data retrieved")
async def get_user_data(name):
    user = await retrieve_user_by_name(name)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")

# For update
@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "user with ID: {} name update is successful".format(id),
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


# For delete
@router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )