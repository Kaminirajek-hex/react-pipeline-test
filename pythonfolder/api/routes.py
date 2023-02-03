from api import testing_entityapi
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.exceptionmiddleware import ExceptionMiddleware
from middleware.loggingmiddleware import LoggingMiddleware

app = FastAPI()

app.add_middleware(ExceptionMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)

app.include_router(testing_entityapi.router, tags=["testing_entity"])
