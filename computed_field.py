from pydantic import BaseModel, Field , EmailStr , computed_field
from typing import Optional, List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]

    @computed_field
    @property
    def cal_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)
    print(patient.cal_bmi)  # computed field
    print("Patient inserted successfully")


Patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 1.75,
    "married": True,
    "allergies": ["dust", "pollen"],
    "contact_info": {"email": "john.doe@example.com"}
}

patient1 = Patient(**Patient_info)

insert_patient(patient1)