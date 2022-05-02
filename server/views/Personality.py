import pickle
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import *
from server.models.accounts import (
    ErrorResponseModel,
    ResponseModel,
    Personality
)

router = APIRouter()

with open(r'B:/intern/quizly-rejoice/model_pkl' , 'rb') as f:
    lr = pickle.load(f)
@router.post("/", response_description="user data added into the database")
async def add_user_data(user: Personality = Body(...)):
    user = jsonable_encoder(user)
    predict=lr.predict([[ user['EXT1'],user['EXT2'],user['EXT3'],user['EXT4'],2,user['EXT6'],user['EXT7'],user['EXT8'],user['EXT9'],user['EXT10'],user['EST1'],4,user['EST3'],user['EST4'],user['EST5'],user['EST6'],user['EST7'],user['EST8'],user['EST9'], 1, 4, 1, 5, 2,5, 2, 4,4,4,4,user['CSN1'],4,user['CSN3'],user['CSN4'],user['CSN5'],4,user['CSN7'],user['CSN8'],4,4,1,5,1,4,1,4,user['OPN7'],user['OPN5'],5,5]])     
    # openness,conscientiousness,Extraversion,Aggreableness,Neurocitism
    if str(predict[0])=="1":
                personality='openness'
    elif str(predict[0])=="2":
        personality='conscientiousness'
    elif str(predict[0])=="3":
        personality='Extraversion'
    elif str(predict[0])=="4":
        personality='Aggreableness'
    else:
        personality='Neurocitism'
    data={"Personality":personality,'flag':1}
    try:
        users = await user_collection.find_one({"_id": ObjectId(user['id'])})
        if users:
            updated_user =  user_collection.update_one(
                {"_id": ObjectId(user['id'])}, {"$set": data}
            )
            msg="Successfully Predicted"
        else:
            msg="User Not Found"
    except:       
        msg="Error ocured "     
    return {"code": 200,"message":msg}
    