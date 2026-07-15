from pydantic import BaseModel, ConfigDict


# Shared fields
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: str


# Used when creating a new patient (POST)
class PatientCreate(PatientBase):
    pass


# Used when updating a patient (PUT)
class PatientUpdate(PatientBase):
    pass


# Used when returning patient data (response)
class PatientResponse(PatientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
