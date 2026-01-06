from fastapi import APIRouter

router_home = APIRouter()

@router_home.get("/")
def controller_welcome():
    return {"welcome": "User"}