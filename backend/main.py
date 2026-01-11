from fastapi import FastAPI
from routers.ask import router_of_ask
from routers.home import router_home
from routers.security import router_security

app=FastAPI(version="1.0.0")

app.include_router(router_security, prefix="/api", tags=["Security"])
app.include_router(router_home, prefix="/api", tags=["Home"])
app.include_router(router_of_ask, prefix="/api", tags=["Ask"])