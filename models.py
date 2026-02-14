from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    incident_type = Column(String)
    description = Column(String)
    location = Column(String)
    risk_level = Column(String)
    status = Column(String, default="SUBMITTED")
    created_at = Column(DateTime, default=datetime.utcnow)