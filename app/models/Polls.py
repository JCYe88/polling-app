from __future__ import annotations
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List, Optional
from .Choices import Choice
from fastapi import HTTPException


class PollCreate(BaseModel):
    """Poll write data model"""
    title: str = Field(min_length=5, max_length=50)
    options: List[str]
    expires_at: Optional[datetime] = None
    
    @field_validator("options")
    @classmethod
    def validate_options(cls, options: List[str]) -> List[str]:
        if len(options) < 2 or len(options) > 5:
            raise HTTPException(
                status_code=400,
                detail="A poll must contain between 2 and 5 choices"
            )
        return options
    
    def create_poll(self) -> Poll:
        """ 
        Create a new Poll instance with auto-incrementing labels for 
        Choices, e.g. 1, 2, 3
        This will be used in the /polls/create endpoint
        """
        choices = [
            Choice(
                description=desc,
                label=index + 1 
            )
            for index, desc in enumerate(self.options) 
        ]
        
        if self.expires_at is not None and self.expires_at <  datetime.now(timezone.utc):
            raise HTTPException(
                status_code=400,
                detail="A poll's expiration must be in future"
            )
        
        return Poll(title=self.title, options=choices, expires_at=self.expires_at)
        
        

class Poll(PollCreate):
    """Poll read data model, with uuid, creation date"""
    id: UUID = Field(default_factory=uuid4)
    options: List[Choice]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    
