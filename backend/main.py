from fastapi import FastAPI
from routers.ask import router_of_ask
from routers.home import router_home
from routers.security import router_security

app=FastAPI()

app.include_router(router_security, tags="api/token")
app.include_router(router_home, tags="api")
app.include_router(router_of_ask, tags="api")
