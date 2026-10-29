from pydantic import BaseModel, EmailStr , Field

class Student(BaseModel):
    name: str ="Sasm"
    age:str
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,description="CGPA should be between 0 and 10",default=7.5)

new_stu={"age":20,"email":"ab@example.com"}
stu=Student(**new_stu)
print(stu.name) 
print(stu.cgpa)

