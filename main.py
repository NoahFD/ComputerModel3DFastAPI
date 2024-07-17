from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai.types.chat import ChatCompletionMessage
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from schemas.message import MessagePrompt

_ = load_dotenv(find_dotenv())
app = FastAPI()
# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/", response_model=ChatCompletionMessage)
async def chat_completion(payload: MessagePrompt):
    client = OpenAI()
    print(payload.prompt)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant.Always reply in less than 30 words and say thank you!"},
            {"role": "user", "content": payload.prompt}
        ],
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    return completion.choices[0].message


@app.get("/hello/{name}", response_model=Item)
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
