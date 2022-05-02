from typing import Optional, List
from datetime import datetime
from xmlrpc.client import Boolean
from pydantic import BaseModel, EmailStr, Field
class UserSchema(BaseModel):
    email: str
    userName: str
    social: bool
    # firstName: str
    # lastName: str
    # middleName: str
    # bio: str
    # gender: str
    # birthDate: str
    # birthMonth:str
    # birthYear: str
    passWords:str
    mobile: str
    flag: int
    Personality:str
    Score:int
    # lastLoginAt: Optional[datetime] = Field(
    #     ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    # lastSessionEndTime: Optional[datetime] = Field(
    #     ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    # createdAt: Optional[datetime] = Field(
    #     ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    # updatedAt: Optional[datetime] = Field(
    #     ..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    # isDeleted: Optional[bool] = True
    class Config:
        schema_extra = {
            "example": {
                "email": "parth@gmail.com",
                "userName": "parth",
                'social':False,
                # "firstName": "parth",
                # "lastName": "patel",
                # "middleName": "p",
                # "bio": "nice",
                # "gender": "Male",
                # "birthDate": "12",
                # "birthMonth": "12",
                # "birthYear": "2022",
                "passWords":"1234",
                "mobile":"1233456789",
                "flag":0,
                "Personality":"None",
                "Score":"0"
                # "lastLoginAt": "2019-04-01T00:00:00.000Z",
                # "lastSessionEndTime": "2019-04-01T00:00:00.000Z",
                # "createdAt": "2019-04-01T00:00:00.000Z",
                # "updatedAt": "2019-04-01T00:00:00.000Z",
                # "isDeleted": "False",
            }
        }
class Login(BaseModel):
    email: str
    passWords:str
    social: Optional[bool]
    # mobile: str
    class Config:
        schema_extra = {
            "example": {
                "email": "parth@gmail.com",
                'social':False,
                "passWords":"1234",
                # "mobile":"1234567809"
               }}
class UpdateUserModel(BaseModel):
    email: Optional[EmailStr]
    userName: Optional[str]
    social: Optional[bool]
    # firstName: Optional[str]
    # lastName: Optional[str]
    # middleName: Optional[str]
    # loginProvider: Optional[str]
    # bio: Optional[str]
    # gender: Optional[str]
    # birthDate: Optional[str]
    # birthMonth: Optional[str]
    # birthYear: Optional[str]
    passWords:Optional[str]
    # mobile:Optional[str]
    # isDeleted: Optional[bool] = True
    class Config:
        schema_extra = {
            "example": {
                "email": "akshit@gmail.com",
                "userName": "iuytfghj",
                'social':False,
                # "firstName": "iuytfdxcvhn",
                # "lastName": "uygfvhjn",
                # "middleName": "uyghj",
                # "bio": "iuytgjhc",
                # "gender": "jytghg",
                # "birthDate": "12",
                # "birthMonth": "3",
                # "birthYear": "2022",
                "password": "1234",
                # "lastLoginAt": "2019-04-01T00:00:00.000Z",
                # "lastSessionEndTime": "2019-04-01T00:00:00.000Z",
                # "createdAt": "2019-04-01T00:00:00.000Z",
                # "updatedAt": "2019-04-01T00:00:00.000Z",
                # "isDeleted": "False",
            }
        }
class Personality(BaseModel):
    id:str
    EXT1:int
    EXT2:int	
    EXT3:int	
    EXT4:int	
    EXT6:int	
    EXT7:int	
    EXT8:int
    EXT9:int
    EXT10:int
    EST1:int		
    EST3:int	
    EST4:int	
    EST5:int	
    EST6:int	
    EST7:int	
    EST8:int	
    EST9:int		
    CSN1:int		
    CSN3:int	
    CSN4:int	
    CSN5:int	
    CSN7:int	
    CSN8:int	
    OPN5:int		
    OPN7:int	

  	
    # mobile: str
    class Config:
        schema_extra = {"example": {
                    "id":'62678f78a5b48f8834798337',
                    'EXT1':'1',
                    'EXT2':'1',	
                    'EXT3':'1',	
                    'EXT4':'1',
                    'EXT6':'1',	
                    'EXT7':'1',	
                    'EXT8':'1',
                    'EXT9':'1',
                    'EXT10':'1',
                    'EST1':'1'	,
                    'EST3':'1'	,
                    'EST4':'1'	,
                    'EST5':'1'	,
                    'EST6':'1'	,
                    'EST7':'1'	,
                    'EST8':'1'	,
                    'EST9':'1'	,
                    'CSN1':'1'	,
                    'CSN3':'1'	,
                    'CSN4':'1'	,
                    'CSN5':'1'	,
                    'CSN7':'1'	,
                    'CSN8':'1'	,
                    'OPN5':'1'	,
                    'OPN7':'1'	
               }}

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
