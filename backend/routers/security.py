# from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Request, BackgroundTasks
from fastapi.responses import RedirectResponse

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from dependencies.get_token_user import TokenUser

from dependencies.token import method_token
from shemal import UserLoginSchema
from dependencies.email import scheme_email


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
        return {"error": f"this is error login: {e}"}
     

@router_security.post("/login_up")
async def login_up(userLoginSchema:UserLoginSchema, backround_tasks: BackgroundTasks):
    try:
        response = await method_token.create_token(sub=userLoginSchema.username)
        
        if not response:
            return {"error": response}
        
        email_response = await scheme_email.create_emai(email_to_send=userLoginSchema.email, token_user=response)    
        
        if not email_response:
            return {"error": email_response}
        
        backround_tasks.add_task(scheme_email.create_emai, email_to_send=userLoginSchema.email, token_user=response)

        return {"message": "Email sent successfully"}
    
    except Exception as e:
        return {"error": f"this is error in login_up: {e}"}
    


@router_security.get("/token/{token}")
async def verify_token(token: str, request: Request):
    try:

        response = await method_token.decode_token(token=token)
        
        if not response:
            return {"error": response}

        return RedirectResponse(url="/api/home")
    
    except Exception as e:
        return {"error": f"this is error in verify_token: {e}"}    