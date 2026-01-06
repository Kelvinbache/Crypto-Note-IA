from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dependencies.get_token_user import TokenUser
from dependencies.token import method_token
from dependencies.email import scheme_email


router_security = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
token_user_dependency = TokenUser(Depends(oauth2_scheme))

@router_security.post("/login")
async def login(request:Request, from_data: OAuth2PasswordRequestForm = Depends()):
     
    response = await method_token.create_token(sub=from_data.username)
    
    if not response:
        return {"error": response}
    
    return {"message": "Login successful"}


@router_security.post("/login_up")
async def login_up(request:Request):
    try:
        data = await request.form()
        response = await method_token.create_token(sub=data.get("username"))
        
        if not response:
            return {"error": response}
        
        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"error": f"this is error in login_up: {e}"}
    