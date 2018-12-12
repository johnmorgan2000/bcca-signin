from django.forms import Form
from django import forms

from signins import models


class SignInForm(Form):
    name = forms.CharField(label="Name")

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']

        if models.Student.is_student_signed_in(name=cleaned_name):
            raise forms.ValidationError('Cannot sign in twice')

        elif models.Student.is_in_current_class(name=cleaned_name) is False:
            raise forms.ValidationError("Is not a current student")

        return cleaned_name


class SignInSince(Form):
    date = forms.DateField(label="Date", input_formats=['%Y-%m-%d'])

    # def clean_date(self):
    #     cleaned_date = self.cleaned_data['date']

    #     if models.Student.get_signins_since(date=cleaned_date) :
    #         raise forms.ValidationError('Not a valid date')

    #     return cleaned_date
