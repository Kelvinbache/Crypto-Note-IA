from fastapi import APIRouter, Request, BackgroundTasks
from fastapi.responses import RedirectResponse
from dependencies.token import method_token
from shemal import UserLoginSchema
from dependencies.email import scheme_email
from db.postgrest import db

router_security = APIRouter()

@router_security.post("/login")
async def login(userLoginSchema:UserLoginSchema):
     try:
        conn = await db.ini_db()
        with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM users 
                    WHERE name_user = %s AND password = %s;
                """, (userLoginSchema.username, userLoginSchema.password))
                
                user = cur.fetchone()
                
                if not user:
                    return {"error": "Invalid username or password"}
                
                if user:
                    response = await method_token.create_token(sub=user[1])
    
                    cur.execute("""
                        SELECT user_id FROM test WHERE user_id = %s;
                    """, (user[0], ))
    
                    test_entry = cur.fetchone()
    
                    if test_entry[0] == user[0]:  
                        return {"message": "Login successful"}
                    else:   
                        cur.execute("""
                            INSERT INTO test (user_id,chat_id, status) VALUES (%s, %s, %s);
                        """, (user[0], user[0], True))
                        
                        conn.commit()
    
                    if not response:
                        return {"error": response}
                    
                    return {"message": "Login successful"}
                
                return {"message": "User not exit"}
                


     except Exception as e:
         return {"error": f"this is error login: {e}"}
             

@router_security.post("/sing_up")
async def login_up(userLoginSchema:UserLoginSchema, backround_tasks: BackgroundTasks):
    try:
        conn = await db.ini_db()        
        with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (name_user, email_user, password)
                    VALUES (%s, %s, %s);
                """, (userLoginSchema.username, userLoginSchema.email, userLoginSchema.password))
                
                conn.commit()

        response = await method_token.create_token(sub=userLoginSchema.username)
        
        if not response:
            return {"error": response}
        
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