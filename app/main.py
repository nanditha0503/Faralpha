from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/sayHello")
async def say_hello():
    return JSONResponse(content={"message": "Hello Nanditha!!"})

@app.post("/submitData")
async def submit(data: dict):
    return {"status": "received", "data": data}

@app.put("/updateItem/{item_id}")
async def update(item_id: int, item: dict):
    return {"status": "updated", "id": item_id, "data": item}


