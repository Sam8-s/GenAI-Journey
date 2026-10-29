from typing import TypedDict

class Person(TypedDict):
    name:str
    age:str

student:Person={"name":"sam","age":"20"}
print(student)