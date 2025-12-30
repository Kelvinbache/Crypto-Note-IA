from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def controller():
  return {"hello":"word"}

