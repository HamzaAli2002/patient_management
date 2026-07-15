from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import patient as patient_crud
from app.schemas.patient import PatientCreate, PatientUpdate, PatientResponse

router = APIRouter(prefix="/patients", tags=["Patients"])


# Create Patient
@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return patient_crud.create_patient(db, patient)


# Get All Patients
@router.get("/", response_model=list[PatientResponse])
def get_all_patients(db: Session = Depends(get_db)):
    return patient_crud.get_all_patients(db)


# Get Patient by ID
@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = patient_crud.get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


# Update Patient
@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    updated_patient = patient_crud.update_patient(db, patient_id, patient)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient


# Delete Patient
@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    deleted_patient = patient_crud.delete_patient(db, patient_id)
    if not deleted_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": f"Patient with id {patient_id} deleted successfully"}
