from fastapi import FastAPI
from routers import components

app = FastAPI()

app.include_router(components.router)

@app.get('/')
def root():
  return 'Hello world'