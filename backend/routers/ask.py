from IA.geminis import ollama_consult
from fastapi import APIRouter
from pydantic import BaseModel

router_of_ask = APIRouter()

class Ask(BaseModel):
    promt:str


@router_of_ask.post("/")
async def controller_consult(data:Ask):
    try:

       consult = ollama_consult.consult(data.promt)
       return {"response": consult}
   
    except Exception as e:
        return f"Type os error:{e}"