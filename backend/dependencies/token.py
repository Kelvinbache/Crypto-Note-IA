from jose import jwt
from datetime import datetime, timedelta, timezone

class Token_generator():
    def __init__(self):
        self.algorithm = "HS256"
        self.secret = "secret"
    
    async def create_token(self, sub:str):
        exp = datetime.now(timezone.utc) + timedelta(minutes=10)
        iat = datetime.now(timezone.utc) 

        try:
            payload = {
            "sub": sub,
            "exp":int(exp.timestamp()),
            "iat":int(iat.timestamp())
            }

            return jwt.encode(payload, self.secret, algorithm=self.algorithm)    

        except Exception as e:
            return f"this is error en create token:{e}"

    async def decode_token(self, token):
        try:
            payload = jwt.decode(token=token,subject=self.secret,algorithms=self.algorithm)
            sub = payload.get("sub")
            
            if not sub:
                return "token is invalid"
            else:
                return sub

        except Exception as e:
            return f"this is error in decode token: {e}"

method_token = Token_generator()        