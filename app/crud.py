from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def create_incident(db: Session, incident: schemas.IncidentCreate):
    # Create new incident with default status
    db_incident = models.Incident(
        description=incident.description,
        source=incident.source,
        status="new"  # Default status
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

def get_incidents(db: Session, status: Optional[str] = None) -> List[models.Incident]:
    # Get all incidents, optionally filtered by status
    query = db.query(models.Incident)
    if status:
        query = query.filter(models.Incident.status == status)
    return query.all()

def get_incident(db: Session, incident_id: int) -> Optional[models.Incident]:
    # Get incident by ID
    return db.query(models.Incident).filter(models.Incident.id == incident_id).first()

def update_incident_status(db: Session, incident_id: int, status: str) -> Optional[models.Incident]:
    # Update incident status by ID
    db_incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if db_incident:
        db_incident.status = status
        db.commit()
        db.refresh(db_incident)
    return db_incident
