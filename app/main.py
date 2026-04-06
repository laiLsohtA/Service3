from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Service 3 running"}