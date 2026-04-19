from pydantic import BaseModel, Field , EmailStr , model_validator
from typing import Optional, Annotated , List , Dict

class Patient(BaseModel):
    name: str
    age: int  
    email: EmailStr  
    weight:float
    married:bool
    allergies:Optional[list[str]] = None # if we add only list then it will accept any type of list, but if we specify list[str] then it will only accept list of strings
    contact_details: dict[str, str] # if we add only dict then it will accept any type of dict, but if we specify dict[str, str] then it will only accept dict with string keys and string values

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact details are required for patients above 60 years old")
        return model
    

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)    
    print(patient.email)
    print("Patient inserted successfully")
Patient_info = {"name": "John Doe", "age": 100,"email":'abc@hdfc.com', "weight": 70.5, "married": True, "contact_details": {"email": "john.doe@example.com"}}

patient1= Patient(**Patient_info)  # This will validate the data and create a Patient instance and type corecion will also happen for name field
insert_patient(patient1)