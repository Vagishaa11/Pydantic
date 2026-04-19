#model ko as a field use karna nested model kehlata hai
from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator

class  Address(BaseModel):
    city: str
    state: str
    pincode: str




class Patient(BaseModel):
    name: str
    gender: str
    age: int  
    address: Address
 
address_dict = {"city": "Mumbai", "state": "Maharashtra", "pincode": "400001"}
address1=Address(**address_dict)  # This will create an instance of Address model
patient_info = {"name": "John Doe", "gender": "Male", "age": 30, "address": address1}
patient1 = Patient(**patient_info)  # This will create an instance of Patient model with nested Address model
# print(patient1)


# exporting nested model to json
# temp=patient1.model_dump()
temp=patient1.model_dump(include=['name','address'])  # This will include only name and city from address in the output   
# exclude bhi hota hai jisme agar hum kisi field ko output me include nahi karna chahte to us field ko exclude kar sakte hai, for example temp=patient1.model_dump(exclude=['age']) isme age field output me include nahi hoga, aur agar hum nested model ke kisi specific field ko include ya exclude karna chahte hai to uske liye dot notation ka use kar sakte hai, for example temp=patient1.model_dump(include=['name','address.city']) isme name aur address ke city field ko output me include karega, aur temp=patient1.model_dump(exclude=['address.pincode']) isme address ke pincode field ko output me include nahi karega.
# exclude unset bhi hota hai jisme agar koi field ka value set nahi hai to wo us field ko output me include nahi karega
print(temp)
print(type(temp))  # This will show that temp is a dictionary





# benefits of nested models:
# 1. Reusability: We can reuse the Address model in multiple places where we need to represent an address, without having to redefine the fields each time.
# 2. Modularity: It helps in organizing the code better by separating concerns. The
# Address model can be maintained independently of the Patient model, making it easier to manage and update.
# 3. Validation: Each model can have its own validation logic, making it easier to
# ensure data integrity. For example, we can add specific validators to the Address model to validate the city, state, and pincode fields without affecting the Patient model.
# 4. Clarity: It makes the code more readable and easier to understand. By using nested models, we can clearly see the relationship between different entities (e.g., a patient has an address) and how they are structured.
