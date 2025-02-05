from fastapi import FastAPI
import sys
import os
import signal

app = FastAPI()

@app.get("/")
async def hello():
    return "hey the server is running :)"

@app.get("/kill")
async def echo_message():
    os.kill(os.getpid(), signal.SIGINT)
    sys.exit(1)
