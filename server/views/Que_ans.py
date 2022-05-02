import json
import random
from fastapi import APIRouter

from server.database import *
from server.models.accounts import (
    ResponseModel,
    ErrorResponseModel
)
category={
    "Maths": ["Accountancy", "commerce NTA NET", "Commerce"],
    "Geography": ["Earth Science", "Geography Map", "GEOLOGY","Indian Geography"],
    "Technology":["Biotechnology"],
    "Sports": [None],
    "Business": ["Buiseness Statistics","Buiseness Studies (VOL 1)","Buiseness Studies (Volume 2)"],
    "Adventure": ["Journalism","Locomotion"],
    "Biology": ["Astrobiology","Backteriology","Backteriology","Animal Kingdom","Biological Classification","cardiovascular NEET","Cell Biology",
                "Cell cycle and cell division","Cell structure and functions","CELL THEORY","Cell Transport","Digestion and absorption",
                "Biology Vol 1","Biology Vol 2","Biology Vol 3","Biology Vol 4","Biology Vol 5","Virology","Biology Vol 6","Biology Vol 7","Biophysics",
                "Microbiology","Microbes","NEET BIOLOGY","Nursing","Nutrition and Minerals (Vol 2)","Nutrition and minerals (Vol1)","Biodiversity","human health disease","Human health"],
    "Dance": [None],
    "Writing": [None],
    "Music": [None],
    "Science": ["Botany","Child development nd pedagogy","ENTOMOLOGY","human health disease","Human health","Pharmacology","Research Methodology",
                "Covid 19","Everyday science"],
    "Physics": ["Biophysics"],
    "Food": ["Food chain","Nutrition and Minerals (Vol 2)","Nutrition and minerals (Vol1)",],
    "Sociology": ["Child development nd pedagogy","Everyday science"],
    "Movies": [None],
    "History": ["History of China","USSR and SOUTHEAST ASIA HISTORY","History of EUROPE","Mediaval India","Mesoamerican","Mesopotamiam civilization","Medieval World","History of India","Indian History","Islamic studies","History of JAPAN"],
    "Tradition": ["Mediaval India","Medieval World","Mesoamerican",],
    "Art": [None],
    "Psychology": [None],
    "Banking":["Banking Awarness 2"],
    "Politics": ["Indian Constitution","Indian Polity","International Relations"],
    "Economics": ["E-Commerce","Economics volume 1","Economics volume 2","Banking Awarness 2","Banking Awarness","Economics volume 3","Economics volume 4"],
    "Finance": ["Financial Management","GST"],
    "Agriculture": ["Agriculture","Pharmacology","Botany","Earth Science","ECology (Volume 1)","ECOLOGY (VOLUME 2)","ENTOMOLOGY","Environment studies volume 2","Histology","Environment volume 1","Environmental issues"],
    "Computer Science": ["Algorithm design","Operating System","Microprocessor","Mobile Computing","Cloud computing","Computer Architecture","Computer Graphics","Machine Learning","Computer Networking","Computer organization","Embedded Systems"],
    "Artificial Intelligence": ["Artificial intelligence","Machine Learning"],
    "Current Affairs": ["Criminal Law","current affairs 2016","current affairs 2017","current affairs 2018","current affairs 2019","current affairs"],
    "Data systems": ["Data Mining","DBMS"],
    "Education": ["Education","Embedded Systems","International Relations","Islamic studies","Teaching and Learning","Teaching Aptitude","Teaching as a profession","Teaching Strategies","CITIZENSHIP TEST"],
    "Social Science": ["Bangla Sahitya","Social  science (Volume 1)","Social science (Volume 2)","Social science (Volume 3)","Social science (Volume 4)","Social science (Volume 5)","Social science (Volume 6)",],
    "Chemistry": ["Inorganic Chemistry","Organic Chemistry","Physical Chemistry","Polymer Chemistry"],
    "English": ["English Literature","Linguistics","Morphology"],
    "Software Design & Engineering": ["Project management","Software ENgineering","Software testing"],
    "Civilization": ["African Civilization","world civilization","World civilization(1)","Persian Civilization","ROMAN CIVILIZATION","AZTEC CIVILIZATION","Incan Civilization","Mayan Civilization","Mesopotamiam civilization"],
    "General Knowlwdge": ["puzzles","Criminal Law","general knowledge","GST","human health disease","Indian Constitution","Intellectual Property"]
}
router = APIRouter()
# f = open(r'D:\apk-sim\QUIZZY\Banking Awarness 2.json')
# data = json.load(f)
# l=[]
# for i in (data["Banking Awarness 2"]).keys():
#     l.append(i)
# ques=[]
# random.shuffle(l)
# for j in l[:10]:
#     ques.append(data["Banking Awarness 2"][j])
# f.close()
# Banking Awarness 2
@router.post("/{categorys}", response_description="Get question answer")
async def get_question_answer(categorys):
    Book=category[categorys]
    ques=[]
    for Subcategory in Book:
        if Subcategory==None:
            break
        book = open(r'D:/apk-sim/QUIZZY/pdf_to_json/'+Subcategory+'.json')
        data = json.load(book)
        Keys=[]
        for items in (data[Subcategory]).keys():
            Keys.append(items)
        
        random.shuffle(Keys)
        for items in Keys[:10]:
            ques.append(data[Subcategory][items])
        book.close()
    random.shuffle(ques)
    ques=ques[:10]
    return ResponseModel(ques, "user data retrieved successfully") 

    
@router.post("/{id}/{Output}/{Score}", response_description="Get question answer")
async def Get_Score(id:str,Output:str,Score:int):
    User=await user_collection.find_one({"_id": ObjectId(id)})
    if User:
        if Output=="Winner":
            score=int(User['Score'])+Score
            
            if score>=100:
                Level="Silver"
            if score>=500:
                Level="Gold"
            if score>=2000:
                Level="Platinum"
            if score<100:
                Level="Bronze"
            data={"Score":score,"Level":Level}
            updated_user =  user_collection.update_one(
                {"_id": ObjectId(User['_id'])}, {"$set": data}
            )
            return {"Msg":data,'Output':Output,"Id": str(ObjectId(User['_id'])),"Score":User["Score"],"Level":User["Level"],"Name":User["userName"]}
        elif Output=="Losser":
            score=int(User['Score'])+Score
            
            if score>=100:
                Level="Silver"
            if score>=500:
                Level="Gold"
            if score>=2000:
                Level="Platinum"
            if score<100:
                Level="Bronze"
            data={"Score":score,"Level":Level}
            updated_user =  user_collection.update_one(
                {"_id": ObjectId(User['_id'])}, {"$set": data}
            )
            return {"Msg":data,'Output':Output,"Id": str(ObjectId(User['_id'])),"Score":User["Score"],"Level":User["Level"],"Name":User["userName"]}
    else:
        return {"msg":"User Not Found"}


@router.get("/{id}")
async def Check_Level(id: str):
    User=await user_collection.find_one({"_id": ObjectId(id)})
    if User:
        if User["Score"]>=100:
            Level="Silver"
        if User["Score"]>=500:
            Level="Gold"
        if User["Score"]>=2000:
            Level="Platinum"
        if User["Score"]<100:
            Level="Bronze"
        data={"Level":Level}
        updated_user =  user_collection.update_one(
                {"_id": ObjectId(User['_id'])}, {"$set": data}
            ) 
        return {"Id": str(ObjectId(User['_id'])),"Score":User["Score"],"Level":User["Level"],"Name":User["userName"]}
         
    return {"msg" :"Error Ocured"}      

@router.get("/Score/{id}")
async def Check_Current_Score(id: str):
    User=await user_collection.find_one({"_id": ObjectId(id)})
    if User:
        return {"Id": str(ObjectId(User['_id'])),"Name":User["userName"],"Score":User["Score"],"Level":User["Level"]}
         
    return {"msg" :"Error Ocured"}      