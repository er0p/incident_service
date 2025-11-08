from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional
from . import models, schemas, crud
from .db import engine, SessionLocal
from .auth import get_current_user

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Incident Tracker",
    description="web-service for tracking various incidents",
    version="1.0.0"
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/incidents/", response_model=schemas.IncidentCreate)
def create_incident(incident: schemas.IncidentCreate, db: SessionLocal = Depends(get_db), username: str = Depends(get_current_user)):
    """Create a new incident"""
    return crud.create_incident(db=db, incident=incident)

@app.get("/incidents/", response_model=List[schemas.IncidentOut])
def get_incidents(
    status: Optional[str] = Query(None, description="Filter by status"),
    db: SessionLocal = Depends(get_db),
    username: str = Depends(get_current_user)
):
    """Get list of incidents with status filter"""
    return crud.get_incidents(db=db, status=status)

@app.get("/incidents/{incident_id}", response_model=schemas.IncidentOut)
def get_incident(incident_id: int,
                 db: SessionLocal = Depends(get_db),
                 username: str = Depends(get_current_user)
                 ):
    """Get incident by ID"""
    db_incident = crud.get_incident(db=db, incident_id=incident_id)
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident

@app.put("/incidents/{incident_id}", response_model=schemas.IncidentOut)
def update_incident_status(
    incident_id: int, 
    status_update: schemas.IncidentUpdate,
    db: SessionLocal = Depends(get_db),
    username: str = Depends(get_current_user)
):
    """Update incident status"""
    db_incident = crud.update_incident_status(
        db=db, 
        incident_id=incident_id, 
        status=status_update.status
    )
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident

@app.get("/")
def root():
    return {"message": "Incident Tracking Service"}

@app.get("/auth-test/")
def auth_test(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}", "authenticated": True}
