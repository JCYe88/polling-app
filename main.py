from fastapi import FastAPI
from app.models.Polls import Poll, PollCreate



app = FastAPI(title="Polls API")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test")
def test():
    return {"message": "hello there"}



@app.post("/polls/create")
def create_poll(poll: PollCreate):
    # return Poll(
    #     title="some placeholder title",
    #     options=["yes", "no", "maybe"]
    # )
    new_poll = poll.create_poll()
    return {
        "detail": "Poll successfully created",
        "poll_id": new_poll.id,
        "poll": new_poll
    }
    

