from fastapi import FastAPI
from routers.ask import router_of_ask
from routers.home import router_home
from routers.security import router_security

app=FastAPI()

app.include_router(router_security, prefix="/api", tags=["token"])
app.include_router(router_home, prefix="/api", tags=["home"])
app.include_router(router_of_ask, prefix="/api", tags=["ask"])