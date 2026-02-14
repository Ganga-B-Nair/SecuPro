from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from schemas import ReportOut
from schemas import ReportUpdate
from init_db import init_db
from models import Report
from schemas import ManualReportCreate, AIReportCreate
from deps import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/")
def home():
    return {"message": "SECUPRO backend running"}


# -------- Manual Report (Mobile App) --------
@app.post("/reports/manual")
def create_manual_report(data: ManualReportCreate, db: Session = Depends(get_db)):
    report = Report(
        source="manual",
        incident_type=data.incident_type,
        description=data.description,
        location=data.location,
        risk_level=data.risk_level,
        status="SUBMITTED",
        created_at=datetime.utcnow()
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return {"report_id": report.id, "message": "Report created"}


# -------- AI Report (Trigger Script) --------
@app.post("/reports/ai")
def create_ai_report(data: AIReportCreate, db: Session = Depends(get_db)):
    report = Report(
        source="ai",
        incident_type=data.incident_type,
        description=data.description,
        location=data.location,
        risk_level=data.risk_level,
        status="SUBMITTED",
        created_at=datetime.utcnow()
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return {"report_id": report.id, "message": "AI report created"}

@app.get("/reports", response_model=List[ReportOut])
def get_reports(db: Session = Depends(get_db)):
    reports = db.query(Report).order_by(Report.created_at.desc()).all()
    return reports
@app.patch("/reports/{report_id}", response_model=ReportOut)
def update_report(report_id: int, data: ReportUpdate, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()

    if not report:
        return {"error": "Report not found"}

    report.status = data.status
    db.commit()
    db.refresh(report)

    return report
@app.get("/reports/{report_id}", response_model=ReportOut)
def get_single_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()

    if not report:
        return {"error": "Report not found"}

    return report
@app.get("/reports/{report_id}", response_model=ReportOut)
def get_single_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()

    if not report:
        return {"error": "Report not found"}

    return report