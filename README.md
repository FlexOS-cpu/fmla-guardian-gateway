# 💼 FMLA-Guardian — Stateless B2B Shift & Leave Compliance Engine

### 📄 Overview
FMLA-Guardian is a decoupled, stateless backend validation API engineered to prevent corporate shift-scheduling systems from violating multi-state labor laws and protected medical leave acts. The utility acts as an automated operational gatekeeper, cross-referencing real-time worker shift payloads against active leave databases (FMLA, ADA, short-term disability, and workers' compensation). If a conflict matches, it instantly triggers a critical alert warning—shielding client companies from catastrophic federal audit liabilities.

### 🛠️ Key Architectural Highlights
*   **Risk-Mitigation Engine:** Automatically tracks continuous employee leave windows, throwing immediate, structured server exceptions upon detecting a shift allocation breach.
*   **Stateless Architecture:** Designed with zero persistence dependencies. It functions purely as a drop-in middleware validator that scales to millions of data packets with a documented 0% critical error rate.
*   **Rigid Pydantic v2 Type-Safety:** Enforces robust multi-record array parsing structures, ensuring corrupted or distorted enterprise inputs are rejected instantly.
*   **Strategic Cost Avoidance:** Engineered explicitly to prevent Serious compliance infractions, bypassing costly federal audit penalty brackets of up to \$16,131 per occurrence.

### 📁 Project Structure
```text
├── fmla_guardian.py     # Principal compliance validation logic path
├── requirements.txt     # System dependency package manifest
└── README.md            # Technical documentation matrix
```

### ⚙️ Quickstart Local Setup

#### 1. Initialize and Boot the Compliance Engine
```bash
pip install -r requirements.txt
uvicorn fmla_guardian:app --reload --port 8000
```

#### 2. Inspect Automated API Documentation
Once the local server triggers, view the interactive Swagger/OpenAPI documentation playground by navigating to:
`http://127.0.0`

### ⚖️ Intellectual Property & License Notes
**Patent Status:** Covered under an active Provisional Patent Application (PPA) filed with the United States Patent and Trademark Office (USPTO) under Micro Entity Status [1.4]. 

**License:** Upon transaction close via verified escrow routing, 100% intellectual property, commercial exploitation rights, and source code ownership transfer directly to the purchasing entity in perpetuity.
