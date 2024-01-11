from typing import Union
import uvicorn
from fastapi import FastAPI
from app.graphql_app.schema import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql", include_in_schema=False)

@app.get("/")
def read_root():
    return {"Hello": "World"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)