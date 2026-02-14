from pydantic import BaseModel
from datetime import datetime


class ManualReportCreate(BaseModel):
    incident_type: str
    description: str
    location: str
    risk_level: str


class AIReportCreate(BaseModel):
    incident_type: str
    description: str
    location: str
    risk_level: str


class ReportOut(BaseModel):
    id: int
    source: str
    incident_type: str
    description: str
    location: str
    risk_level: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
class ReportUpdate(BaseModel):
    status: str