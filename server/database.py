import motor.motor_asyncio
from bson.objectid import ObjectId
from passlib.context import CryptContext
from server.models.accounts import ResponseModel

MONGO_DETAILS = "mongodb+srv://parth:Parth370@cluster0.df8hf.mongodb.net/parth?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Users
user_collection = database.get_collection("users_collection")
user_description_collection = database.get_collection("users_details")

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)

def user_helper(user) -> dict:
    return {
        "email": user["email"],
        "userName": user["userName"],
        # "firstName": user["firstName"],
        # "lastName": user["lastName"],
        # "middleName": user["middleName"],
        "password":user["passWords"],
        "mobile":user["mobile"]
        # "bio": user["bio"],
        # "gender": user["gender"],
        # "birthDate": user["birthDate"],
        # "birthMonth":user['birthMonth'],
        # "birthYear": user["birthYear"],     
        # "lastLoginAt": user["lastLoginAt"],     
        # "createdAt": user["createdAt"],
        # "updatedAt": user["updatedAt"],
        # "isDeleted": user["isDeleted"]
    }

def user_details(user) -> dict:
    return {
        "_id":str(user["_id"]),
        "email": user["email"],
        "Personality": user["personality"],
        "flag":user["flag"] }

def all_user_helper(user) -> dict:
    return {
        "_id":str(user["_id"]),
        "email": user["email"],
        "userName": user["userName"],
        "mobile":user["mobile"],
        "flag":user["flag"],
        "Personality":user["Personality"]
        # "firstName": user["firstName"],
        # "lastName": user["lastName"],
        # "middleName": user["middleName"],
        
        # "bio": user["bio"],
        # "gender": user["gender"],
        # "birthDate": user["birthDate"],
        # "birthMonth":user['birthMonth'],
        # "birthYear": user["birthYear"],   
        }

# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(all_user_helper(user))
    return users

async def add_user_by_social(user_data: dict) -> dict:
    new_user_email = await user_collection.find_one({"email": user_data["email"]})
    if new_user_email:
        return "email already present"
    user = await user_collection.insert_one(user_data)
    new_user_id = await user_collection.find_one({"email": user_data["email"]})
    _id=str(new_user_id["_id"])
    return  _id
# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    new_user_email = await user_collection.find_one({"email": user_data["email"]})
    new_user_mobile = await user_collection.find_one({"mobile": user_data["mobile"]})
    try :
        if new_user_email:
            return "email already present"
        elif new_user_mobile:
            return "mobile already present"
        else:
            user = await user_collection.insert_one(user_data)
            new_user_id = await user_collection.find_one({"email": user_data["email"]})
            _id=str(new_user_id["_id"])
    except:
        user = await user_collection.insert_one(user_data)
        new_user_id = await user_collection.find_one({"email": user_data["email"]})
        _id=str(new_user_id["_id"])
    return  _id

# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return all_user_helper(user)

async def retrieve_user_by_name(name: str) -> dict:
    print(name)
    user = await user_collection.find_one({"userName": name})
    if user:
        return all_user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True



