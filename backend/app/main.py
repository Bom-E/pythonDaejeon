from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware
    , allow_origins = ["http:localhost:3000"]
    , allow_credentials = True
    , allow_methods = ["*"]
    , allow_headers = ["*"]
)

@app.get("/")
#async def root():
def root():
    return {"message" : "Hello World"}

@app.get("/home")
def home():
    return {"message" : "home"}