from fastapi import FastAPI

app = FastAPI()

@app.get("/{chzexy}")
async def root(chzexy):
    return {"greeting": chzexy, "message": "Welcome to FastAPI!"}
