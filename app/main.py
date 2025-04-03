from fastapi import FastAPI
from .routers import default, auth


app = FastAPI()

app.include_router(auth.router)
app.include_router(default.router)