from multiprocessing.connection import wait
from psycopg2 import connect
import websockets
import asyncio
from fastapi import APIRouter
datas=[
      {
        "Question": "561. Paying the minimum payment on a credit card every month will:",
        "Options": {
          "A": "Pay large percentage of the total balance owed every month",
          "B": "Make the ﬁnal amount paid sub- stantially higher than the amount ini- tially charged to the card",
          "C": "help the cardholder create plan for paying of credit card in decent amount of time",
          "D": "allow the cardholder to avoid pay- ing any interest charges"
        },
        "ans": "B"
      },
      {
        "Question": "269. Money used in exchange for goods and services needed by individuals, businesses, and governments.",
        "Options": {
          "A": "Store of value",
          "B": "Unit of value",
          "C": "Bond",
          "D": "Medium of exchange"
        },
        "ans": "D"
      },
      {
        "Question": "187. At a Railway station, you withdraw cash from ATM of HDFC. HDFC is a",
        "Options": {
          "A": "Paying Banker",
          "B": "Collecting Banker",
          "C": "Advising Banker",
          "D": "Issuing Banker"
        },
        "ans": "A"
      },
      {
        "Question": "131. A deposit account at a ﬁnancial insti- tution that allows consumers to make deposits, pay bills, and make with- drawals",
        "Options": {
          "A": "Savings Account",
          "B": "Checking Account",
          "C": "Credit Union",
          "D": "Bank"
        },
        "ans": "B"
      },
      {
        "Question": "519.",
        "Options": {
          "A": "credit card",
          "B": "chequing",
          "C": "savings",
          "D": "deposit"
        },
        "ans": "A"
      },
      {
        "Question": "69. A movement of money from one ac- count to another is called",
        "Options": {
          "A": "income",
          "B": "fee",
          "C": "annual",
          "D": "transfer"
        },
        "ans": "D"
      },
      {
        "Question": "192. What type of endorsement would you use to deposit your check into your account?",
        "Options": {
          "A": "Endorsement in full",
          "B": "Restrictive endorsement",
          "C": "Blank endorsement"
        },
        "ans": "B"
      },
      {
        "Question": "214. apart for cash deposits, Green chan- nel counters have been enabled for",
        "Options": {
          "A": "funds transfer",
          "B": "registration for MBS",
          "C": "cah withdrawls",
          "D": "all of these"
        },
        "ans": "D"
      },
      {
        "Question": "670. The largest denomination of US cur- rency ever circulated was",
        "Options": {
          "A": "$10,000",
          "B": "1000",
          "C": "100",
          "D": "500"
        },
        "ans": "A"
      },
      {
        "Question": "265. Which of the following changes by the central bank can increase the money supply",
        "Options": {
          "A": "increase in repo rate",
          "B": "increase in CRR",
          "C": "Sale of government securities in the open market",
          "D": "Purchase of government securities in the open market"
        },
        "ans": "D"
      }
    ]
PORT=8000
import nest_asyncio
Room_id="123"
dic={"1":"ok","2":"34343"}
print("Server"+str(PORT))
connected=set()
router = APIRouter()

async def echo(websocket,path):
	print("A client just connected",)
	connected.add(websocket)
	try:
		co=0
		async for message in websocket:
			# 
			strings=str(message).split()
			print("Room id"+strings[0])
			if Room_id==strings[0]:
				
				if co==0:
					await websocket.send("ok"+" "+str(co))
				else:
					await websocket.send(datas[co]["Question"])
				
				co=co+1
				if co==11:
					break
				# if len(connected)==2:
				# 	await conn.send("ok for loop")
						
				pass	
			else:
				break
	except:
		flag=0
		print("connection failed")
@router.get("/", response_description="Get question answer")
async def echos():
  start_server=websockets.serve(echo,'localhost',PORT)
  nest_asyncio.apply()
  asyncio.get_event_loop().run_until_complete(start_server)
  asyncio.get_event_loop().run_forever()