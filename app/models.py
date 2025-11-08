from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
import enum
from datetime import datetime
from .db import Base

#class Incident(Base):
#    __tablename__ = "incidents"
#
#    id = Column(Integer, primary_key=True, index=True)
#    description = Column(String, nullable=False)
#    status = Column(String, default="open")
#    source = Column(String, nullable=False)
#    created_at = Column(DateTime(timezone=True), server_default=func.now())
class IncidentStatus(str, enum.Enum):
    new = "new"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class IncidentSource(str, enum.Enum):
    operator = "operator"
    monitoring = "monitoring"
    partner = "partner"

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.new, nullable=False)
    source = Column(Enum(IncidentSource), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
#    created_at = Column(DateTime(timezone=True), server_default=func.now())
