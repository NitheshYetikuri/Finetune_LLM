import ollama
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio

class Request(BaseModel):
    query: str

app = FastAPI()

def ollama_generate_sync(model: str, prompt: str):
    return ollama.generate(model=model, prompt=prompt)

@app.post("/generate/")
async def create_item(request: Request):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None, ollama_generate_sync, 'finetuned_model:latest', request.query
    )
    result = response.get('response', response)
    return JSONResponse(content={"response": result})

