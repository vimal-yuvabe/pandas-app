from fastapi import FastAPI

app = FastAPI()
# added a comment
@app.get("/")
def read_root():
    return {"Hello": "World this is a test"}