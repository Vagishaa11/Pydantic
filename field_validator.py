from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator
from typing import List ,Dict  ,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int  
    email: EmailStr  
    weight:float
    married: bool
    allergies:Optional[list[str]] = None # if we add only list then it will accept any type of list, but if we specify list[str] then it will only accept list of strings
     # if we add only dict then it will accept

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()  # This will convert the name to title case (e.g., "john doe" -> "John Doe")
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age must be between 0 and 100")




def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)    
    print(patient.email)
    print("Patient inserted successfully")
Patient_info = {"name": "John Doe", "age": "30","email":'abc@hdfc.com', "weight": 70.5, "married": True, "contact_details": {"email": "john.doe@example.com"}}

patient1= Patient(**Patient_info)  # This will validate the data and create a Patient instance and type corecion will also happen for name field
insert_patient(patient1)