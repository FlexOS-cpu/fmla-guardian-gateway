from datetime import date
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="FMLA-Guardian Core Engine",
    description="Stateless middleware utility validating workforce shift scheduling against protected medical leave tracking windows.",
    version="1.0.0"
)

class ShiftAssignment(BaseModel):
    employee_id: str = Field(..., description="Unique global employee workforce identification token.")
    shift_date: date = Field(..., description="The targeted calendar date for the scheduled shift assignment.")
    scheduled_hours: float = Field(..., gt=0.0, le=24.0, description="Total requested shift length.")

class ActiveLeaveRecord(BaseModel):
    employee_id: str
    leave_classification: str = Field(..., description="Protected category signature: FMLA, ADA, STD, or Workers_Comp.")
    leave_start_date: date
    leave_end_date: date

class ValidationMatrixPayload(BaseModel):
    proposed_shift: ShiftAssignment
    active_leave_registry: List[ActiveLeaveRecord]
    custom_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Custom metadata for enterprise log analytics.")

@app.post(
    "/api/v1/compliance/verify-shift",
    status_code=status.HTTP_200_OK,
    summary="Stateless Shift Compliance Auditor"
)
async def verify_shift_eligibility(payload: ValidationMatrixPayload):
    shift = payload.proposed_shift
    
    # SYSTEM INTERCEPTION LOOP
    # Checks every single active leave tracking window to catch scheduling friction immediately
    for record in payload.active_leave_registry:
        if record.employee_id == shift.employee_id:
            if record.leave_start_date <= shift.shift_date <= record.leave_end_date:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail={
                        "error": "CRITICAL_LABOR_COMPLIANCE_VIOLATION",
                        "reason": f"Employee is legally protected under active {record.leave_classification} tracking windows.",
                        "statutory_liability_exposure": "Potential Federal FMLA/OSHA Fine Bracket: Up to $16,131 per infraction."
                    }
                )
                
    return {
        "status": "APPROVED",
        "compliance_check_status": "PASSED",
        "execution_matrix": {
            "employee_id": shift.employee_id,
            "verified_shift_date": shift.shift_date,
            "enforced_action": "ALLOW_SHIFT_PROVISIONING_AND_UPDATE_ROSTER"
        }
    }
