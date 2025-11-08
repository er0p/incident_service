from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .models import IncidentStatus, IncidentSource


class IncidentCreate(BaseModel):
    description: str
    source: IncidentSource


class IncidentUpdate(BaseModel):
    status: IncidentStatus


class IncidentOut(BaseModel):
    id: int
    description: str
    status: IncidentStatus
    source: IncidentSource
    created_at: datetime

    class Config:
        orm_mode = True


#class IncidentBase(BaseModel):
#    description: str
#    source: str
#
#class IncidentCreate(IncidentBase):
#    pass
#
#class IncidentStatusUpdate(BaseModel):
#    status: str
#
#class Incident(IncidentBase):
#    id: int
#    status: str
#    created_at: datetime
#
#    class Config:
#        from_attributes = True
