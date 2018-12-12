from django.db import models
from django.utils import timezone
from django.db.models import Count

# Create your models here.
current_class = [
    'Cole Anderson',
    'Timothy Bowling',
    'Logan Harrell',
    'Ginger Keys',
    'Matt Lipsey',
    'Myeisha Madkins',
    'Henry Moore',
    'John Morgan',
    'Danny Peterson',
    'Ray Turner',
    'Cody van der Poel',
]


class Student(models.Model):
    name = models.TextField()
    date = models.DateField(auto_now_add=True)

    @staticmethod
    def is_student_signed_in(name):
        return Student.objects.filter(name=name, date=timezone.now()).exists()

    @staticmethod
    def signins_for_today():
        return Student.objects.filter(date=timezone.now())

    @staticmethod
    def is_in_current_class(name):
        if name in current_class:
            return True
        return False

    @staticmethod
    def get_signins_since(date):
        # print(
        #     Student.objects.values('name').filter(date__gte=date).annotate(
        #         num=Count('name')).order_by('-num').query)
        return Student.objects.values('name').filter(date__gte=date).annotate(
            num=Count('*')).order_by('-num')

    @staticmethod
    def sign_in(name):
        student = Student(name=name)
        student.save()
        return student
