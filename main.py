from fastapi import FastAPI
from app.api.polls import router

app = FastAPI(
    title="Polls API",
    description="A simple API to create and vote on polls",
    version="0.1",
    openapi_tags=[
        {
            "name": "polls",
            "description": "Operations related to creating and viewing polls"
        }
    ]
    )

app.include_router(router, prefix="/polls", tags=["polls"])


@app.get("/health")
def health():
    return {"status": "ok"}


