from fastapi import FastAPI
from server.views.User_CRUD import router as UserRouter
from server.views.Personality import router as UserPredict
from server.views.Que_ans import router as Ques_Ans
from server.views.web_socket import router as Web
from server.views.server import router as Server
from fastapi.middleware.cors import CORSMiddleware
app= FastAPI()


#staring page route
@app.get("/")
def home():
    return {"Welcome to Quizzy"}

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#add/delete /update /get user details
app.include_router(UserRouter, tags=["User"], prefix="/user")
# app.include_route(UserPredict, tags=["Predict"], prefix="/Predict")
app.include_router(Ques_Ans, tags=["Ques"], prefix="/Ques")
app.include_router(Web, tags=["Web"], prefix="/Web")
app.include_router(Server, tags=["Server"], prefix="/Server")
