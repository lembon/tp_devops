from ninja import NinjaAPI, Schema
from datetime import date
from courses.models import Student, Course
from django.shortcuts import get_object_or_404
from typing import List

api = NinjaAPI()


class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    message: str

@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user

class StudentIn(Schema):
    first_name: str
    last_name: str
    course_id: int = None
    birthdate: date = None
    
class StudentOut(Schema):
    id: int
    first_name: str
    last_name: str
    course_id: int = None
    birthdate: date = None
    
@api.post("/students")
def create_student(request, payload: StudentIn):
    student = Student.objects.create(**payload.dict())
    return {"id": student.id}

    
@api.get("/students/{student_id}", response=StudentOut)
def get_student(request, student_id: int):
    student = get_object_or_404(Student, id=student_id)
    return student


@api.get("/students", response=List[StudentOut])
def list_students(request):
    qs = Student.objects.all()
    return qs

@api.put("/students/{student_id}")
def update_student(request, student_id: int, payload: StudentIn):
    student = get_object_or_404(Student, id=student_id)
    for attr, value in payload.dict().items():
        setattr(student, attr, value)
    student.save()
    return {"success": True}

@api.delete("/students/{student_id}")
def delete_student(request, student_id: int):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return {"success": True}


class CourseIn(Schema):
    title: str
    
class CourseOut(Schema):
    id: int
    title: str
    
@api.post("/courses")
def create_course(request, payload: CourseIn):
    course = Course.objects.create(**payload.dict())
    return {"id": course.id}

    
@api.get("/courses/{course_id}", response=CourseOut)
def get_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    return course


@api.get("/courses", response=List[CourseOut])
def list_courses(request):
    qs = Course.objects.all()
    return qs

@api.put("/courses/{course_id}")
def update_course(request, course_id: int, payload: CourseIn):
    course = get_object_or_404(Course, id=course_id)
    for attr, value in payload.dict().items():
        setattr(course, attr, value)
    course.save()
    return {"success": True}

@api.delete("/courses/{course_id}")
def delete_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return {"success": True}