from django.test import TestCase
from django.urls import reverse
from .models import Course, Student
import json

class StudentDisplayStringTestCase(TestCase):

    def test_student_display_string(self):
        course = Course.objects.create(title="Titulo del curso")
        student = Student.objects.create(first_name="Nombre", last_name="Apellido", course=course)
        self.assertEqual(str(student), 'Apellido, Nombre')


class StudentPostTestCase(TestCase):

    def test_post(self):
        url = reverse('api-1.0.0:create_student')
        course = Course.objects.create(title='Test course')
        student_json = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "course_id": str(course.id),
            "birthdate": "2023-10-29"
        }
        response = self.client.post(url, json.dumps(student_json), content_type='application/json')
        self.assertEquals(200, response.status_code)
