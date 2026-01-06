from typing import Annotated
from dependencies.token import method_token

class TokenUser:
    def __init__(self, OAuth2):
             self.OAUth2 = OAuth2

    def get_token_user(self):
        async def __init__(token: Annotated[str, self.OAUth2]):
            data = method_token.decode_token(token)

            if not data:
                return "Invalid token"
            
            else:
                return data
                    