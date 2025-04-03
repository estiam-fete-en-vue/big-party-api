from fastapi import FastAPI
from .routers import default, auth, payments


app = FastAPI(
  redoc_url="/",
  docs_url=None
)

app.include_router(auth.router)
app.include_router(payments.router)
app.include_router(default.router)