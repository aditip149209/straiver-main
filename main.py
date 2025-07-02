from fastapi import FastAPI, Depends
from sqlmodel import *
from .db import engine
import os
from contextlib import asynccontextmanager

@asynccontextmanager 
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")










