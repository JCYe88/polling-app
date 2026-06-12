from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from datetime import datetime


class VoterCreate(BaseModel):
    email: EmailStr


class Voter(VoterCreate):
    """The Voter read model"""
    voted_at: datetime = Field(default_factory=datetime.now)


class Vote(BaseModel):
    """The Vote read model"""
    poll_id: UUID
    choice_id: UUID
    voter: Voter


class VoteByID(BaseModel):
    choice_id: UUID
    voter: VoterCreate

    
class VoteByLabel(BaseModel):
    choice_label: int
    voter: VoterCreate

