from fastapi import FastAPI
from app.api.v1.router import router
from app.core.database import engine
from app.models.base import Base

app = FastAPI(title="LinkedIn Insights Microservice")

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api/v1")
