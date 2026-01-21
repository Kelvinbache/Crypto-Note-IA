from IA.geminis import ollama_consult
from fastapi import APIRouter
from db.postgrest import db
from shemal import TaskSchema

router_of_ask = APIRouter()


@router_of_ask.post("/ask")
async def controller_consult(data:TaskSchema):
    try:
       conn = await db.ini_db()
       consult = ollama_consult.consult(data.prompt)
       with conn.cursor() as cur:
            cur.execute("""
             INSERT INTO chat (chat) VALUES (%s);
           """, (consult,))
            conn.commit()
          
       return {"response": consult}
   
    except Exception as e:
        return f"Type os error:{e}"