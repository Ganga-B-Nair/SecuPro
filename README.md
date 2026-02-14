<p align="center">
  <img src="./img.png" alt="SecuPro Banner" width="100%">
</p>

# SecuPro 🛡️

### Proactive Workplace Safety & Harassment Prevention System

---

## Team Name

**[Add your team name]**

## Team Members

* **Ganga B Nair** — Mar Baselios College of Engineering and Technology
* **Calvina Anand** — Mar Baselios College of Engineering and Technology

---

## Project Description

SecuPro is a proactive workplace safety platform that transforms traditional complaint-based reporting into an automated prevention system.

Instead of waiting for victims to report incidents, SecuPro detects suspicious behaviour patterns and automatically creates structured HR reports. Employees can also submit anonymous reports safely, ensuring both human and AI-assisted monitoring work together.

---

## The Problem

Workplace harassment frequently goes unreported due to:

* Fear of retaliation
* Lack of evidence
* Social hierarchy pressure
* Slow HR processes

Organizations today react *after damage happens*.

---

## The Solution

SecuPro shifts workplace safety from **reactive → preventive**.

The system:

1. Allows anonymous employee reporting
2. Simulates AI detection from CCTV behaviour analysis
3. Automatically generates structured HR cases
4. Assigns risk level and escalation
5. Enables HR verification workflow

---

## Key Concept

**Detect → Record → Escalate → Verify → Act**

---

## Technologies Used

### Software

* **Frontend:** React + Vite + Tailwind CSS
* **Backend:** FastAPI (Python)
* **Database:** SQLite
* **API Testing:** Swagger UI
* **AI Simulation:** Python trigger script (YOLO-like detection simulation)

### Tools

* VS Code
* Git & GitHub
* Android Studio (optional mobile demo)
* Postman / Swagger

---

## Features

* Anonymous incident reporting
* AI-triggered automatic report creation
* HR Admin dashboard
* Risk classification (Low / Medium / High)
* Status workflow:

  * Pending
  * Under Review
  * Escalated
  * Closed
  * False AI Hallucination
* Real-time dashboard updates
* Structured incident storage

---

## System Architecture

Employee / AI Trigger → FastAPI Backend → Database → HR Dashboard

---

## Installation & Run

### Backend

```bash
cd SecuPro
venv\Scripts\activate
uvicorn main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

### Frontend Dashboard

```bash
cd frontend
npm install
npm run dev
```

Open:

```
http://localhost:5173
```

---

### Trigger AI Detection

```bash
python trigger_ai.py
```

---

## Demo Workflow

1. Create manual report from Swagger
2. Observe dashboard update
3. Run AI trigger
4. Automatic case appears
5. Escalate risk
6. Mark false positive

---

## Screenshots

(Add screenshots here)

---

## Future Scope

* Real YOLOv8 behavioural detection
* Live CCTV integration
* Security alert notifications
* Heatmap risk analytics
* Compliance reporting for organizations

---

## Impact

SecuPro enables organizations to act before incidents escalate, protecting employees and improving workplace culture through early intervention.

---

## AI Tools Used

Used for development assistance and debugging guidance.

---

## Team Contributions

* **Ganga B Nair:** Backend development, database logic, system integration
* **Calvina Anand:** UI/UX design, frontend implementation, workflow design

---

Made with ❤️ at TinkerHub Hackathon
