what is pydantic?


Field Validator :
aapke filed ke uppr custom data validation and transformation apply kr skye @feildvalidator
ek class method hoti hhai @clsmethod

2 mode me operate karta hai
before and after

@feild_validator('name',mode="before")
type coresion ke pehele ki value milegi

mode after  me baad ki

ek single field pe valid krta hai

but for multiple we use modelvalidator