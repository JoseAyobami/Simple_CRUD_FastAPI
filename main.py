from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        "name": "Ana",
        "age": "26",
        "year": "year 1999"
    }
}

class Students(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int]  = None
    year: Optional[str]  = None


@app.get("/")
def home():
    return {"Message" : "Welcome to this simple webserver, this is my first API"}

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(..., description="The id of the student i want to view")):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id : int, name : Optional[str] = None ):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{stuent_id}")
def create_student(student_id : int, student : Students):
    if student_id in students:
        return {"Error": "Student exist"}
    
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doest not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]   


@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int, ):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Messgae": "Student deleted successfully"}
