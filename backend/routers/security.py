# from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Request

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from dependencies.get_token_user import TokenUser

from dependencies.token import method_token
from shemal import UserLoginSchema


router_security = APIRouter()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# token_user_dependency = TokenUser(Depends(oauth2_scheme))

@router_security.post("/login")
async def login(userLoginSchema:UserLoginSchema):
     try:
        response = await method_token.create_token(sub=userLoginSchema.username)
        
        if not response:
            return {"error": response}
        
        return {"message": "Login successful"}
    
     except Exception as e:
        return {"error": f"this is error in login_up: {e}"}
     

@router_security.post("/login_up")
async def login_up(userLoginSchema:UserLoginSchema):
    try:

        response = await method_token.create_token(sub=userLoginSchema.username)
        
        if not response:
            return {"error": response}
        
        return {"message": "Email sent successfully"}
    
    except Exception as e:
        return {"error": f"this is error in login_up: {e}"}
    