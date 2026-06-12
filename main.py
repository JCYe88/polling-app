from fastapi import FastAPI
from app.api.polls import router

app = FastAPI(title="Polls API")

app.include_router(router, prefix="/polls", tags=["polls"])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test")
def test():
    return {"message": "hello there"}
