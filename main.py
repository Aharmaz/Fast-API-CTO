from asyncio import run_coroutine_threadsafe
from fastapi import FastAPI 

from api import users, devices
from db.db_setup import engine
from db.models import device, user
from fastapi.middleware.cors import CORSMiddleware


user.Base.metadata.create_all(bind=engine)
device.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

app.include_router(users.router)
app.include_router(devices.router)