from fastapi import FastAPI
from routers import services

app = FastAPI()

app.include_router(services.router)

@app.get('/')
def root():
  return 'Hello world'