from fastapi import FastAPI

from app.api import patient

app = FastAPI(title="Patient Management System")

app.include_router(patient.router)


@app.get("/")
def root():
    return {"message": "Patient Management System API is running"}
