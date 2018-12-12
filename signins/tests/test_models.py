from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from ..models import Student


class TestIsStudentSignedIn(TestCase):
    def test_nate_is_not_signed_in(self):
        self.assertFalse(Student.is_student_signed_in(name="nate"))

    def test_nate_is_signed_in(self):
        Student.objects.create(name="nate", date=timezone.now())

        self.assertTrue(Student.is_student_signed_in(name="nate"))

    def test_nate_from_yesterday_is_not_signed_in(self):
        yesterday = timezone.now() - timedelta(days=1)
        student = Student.objects.create(name="nate")
        student.date = yesterday
        student.save()

        self.assertFalse(Student.is_student_signed_in(name="nate"))

    def test_is_nate_signed_in_today(self):
        Student.objects.create(name='Henry', date=timezone.now())

        self.assertFalse(Student.is_student_signed_in(name='John'))
