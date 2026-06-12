from fastapi import APIRouter, HTTPException
from app.models.Polls import Poll, PollCreate
from app.services import utils
from uuid import UUID


router = APIRouter()


@router.post("/create")
def create_poll(poll: PollCreate):
    new_poll = poll.create_poll()
    utils.save_poll(new_poll) # Save poll
    
    return {
        "detail": "Poll successfully created",
        "poll_id": new_poll.id,
        "poll": new_poll
    }
    

@router.get("/{poll_id}")
def get_poll(poll_id: UUID) -> Poll:
    poll = utils.get_poll(poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail=f"poll id {str(poll_id)} not found")
    return poll