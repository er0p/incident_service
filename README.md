# Incident Tracker Service

Web service for incident tracking. Allows creating, viewing and updating incident statuses.

# How to Run

## 1. Clone the repository:
```
git clone git@github.com:er0p/incident_service.git
cd incident_service
```
## 2. Create virtual environment
```
python3 -m venv incident
source incident/bin/activate
```
## 3. Install dependencies
```
pip3 install -r requirements.txt
```
## 4. Start the server
```
BASIC_AUTH_USERS="user:password" uvicorn app.main:app --reload
```
# Documentation

The API will be available at: http://localhost:8000

Swagger docs: http://localhost:8000/docs

# Usage Examples

## Create incident
curl -u user:password -X POST "http://localhost:8000/incidents/" \
     -H "Content-Type: application/json" \
     -d '{"description":"Point not responding","source":"monitoring"}'

## Get all new incidents
curl -u user:password "http://localhost:8000/incidents/?status=new"

## Update status
curl -u user:password -X PUT "http://localhost:8000/incidents/1" \
     -H "Content-Type: application/json" \
     -d '{"status":"in_progress"}'

# API Endpoints
_POST /incidents/ - Create new incident_

_GET /incidents/ - Get incidents list (with optional status filter)_

_GET /incidents/{id} - Get incident by ID_

_PUT /incidents/{id} - Update incident status_
