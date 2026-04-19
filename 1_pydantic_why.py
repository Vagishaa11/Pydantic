# def insert_patient(name,age):
#     # Imagine this function interacts with a database to insert a patient record
#     print(name,age)  
#     print("Patient inserted successfully")
# insert_patient("John Doe", 30) 
# This would work, but what if we pass incorrect data types?
# insert_patient("Jane Doe", "thirty")  
# This would cause an error 

# It's not scalable to manually check data types for every function, 
#especially as the codebase grows.
#This is where Pydantic comes in handy, as it provides a way to enforce data types and 
# validate data automatically.

# problems without pydantic:    
# 1. Lack of data validation: Without Pydantic, you would need to manually validate the data being passed to your functions, which can lead to errors and inconsistencies.
# 2. Increased boilerplate code: You would need to write additional code to handle data validation and type checking, which can make your code more verbose and harder to maintain.
# 3. Reduced readability: The lack of clear data models can make it harder for developers to understand the structure of the data being used in the application, leading to confusion and potential bugs.
# 4. Difficulty in handling complex data structures: Without Pydantic, managing and validating complex data structures can become cumbersome and error-prone, especially as the application grows in complexity.
# Overall, not using Pydantic can lead to a less robust and maintainable codebase, making it more difficult to ensure data integrity and consistency throughout the application.

# def insert_patient(name: str, age: int):
#     if type(name)== str and type(age)==int:
#         print(name)
#         print(age)
#         print("Patient inserted successfully")
#     else:
#         raise TypeError("Invalid data types for name or age")
# insert_patient("John Doe", 30)  # This would work
# insert_patient("Jane Doe", "thirty")  # This would raise a TypeError

# how pydantic can help:
# steps:
# 1. Define a Pydantic model to represent the patient data. This model will specify the expected data types for each field.
# 2. Use the Pydantic model to validate the data when inserting a patient.                          
# 3. If the data is valid, proceed with the insertion. If not, Pydantic will raise a validation error, which can be handled appropriately.
#  By using Pydantic, you can ensure that the data being passed to your functions is always of the correct type, reducing the likelihood of errors and improving the overall robustness of your code.

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List ,Dict  ,Optional,Annotated
class Patient(BaseModel):
    name: str
    age: int  
    weight: Annotated[float, Field(gt=0, description="Weight of the patient in kg",strict=True)]  # weight must be a positive float
    married: Annotated[bool, Field(description="Marital status of the patient")]  
    # married must be a boolean value
    allergies:Optional[list[str]] = None # if we add only list then it will accept any type of list, but if we specify list[str] then it will only accept list of strings
    contact_details: dict[str, str] # if we add only dict then it will accept any type of dict, but if we specify dict[str, str] then it will only accept dict with string keys and string values

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)    
    print(patient.contact_details)
    print("Patient inserted successfully")

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient updated successfully")
 
Patient_info = {"name": "John Doe", "age": 30, "weight": 70.5, "married": True, "contact_details": {"email": "john.doe@example.com"}}

patient1= Patient(**Patient_info)  # This will validate the data and create a Patient instance
insert_patient(patient1)  # This would work
#update_patient(patient1)  # This would work

# data validation with pydantic:
# choice 1
# If we try to create a Patient instance with invalid data, Pydantic will raise a validation error
# for email custom data type we can use pydantic's EmailStr type
# from pydantic import EmailStr
# for url custom data type we can use pydantic's HttpUrl type
# from pydantic import HttpUrl

# choice 2
#field function 
# used in pydantic models to provide additional validation and constraints on the fields.
# To attach metadata to a field, you can use the Field function from pydantic. This allows you to specify constraints such as maximum length for strings, or greater than/less than for numbers.

# gt: greater than
# lt: less than
# ge: greater than or equal to
# from pydantic import Field
# class Patient(BaseModel): 
#     name: str = Field(..., max_length=100)  # name must be a non-empty string
#     age: int = Field(..., gt=0)  # age must be greater than 0
#     weight: float = Field(..., gt=0)  # weight must be greater than 0

# annotated types:
#name: Annotated[str, Field(..., max_length=100 , title="Name",example="John Doe")]  # name must be a non-empty string
#age: Annotated[int, Field(..., gt=0,description="Age of the patient")]  # age must be greater