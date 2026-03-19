from fastapi import FastAPI, HTTPException, Depends
from app.routes import accounts, health
from app.db import engine, Base
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AtomBank Account Services", version="2.8.0")

app.include_router(health.router)
app.include_router(accounts.router, prefix="/accounts")

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    logger.info("Account Services v2.8.0 started")