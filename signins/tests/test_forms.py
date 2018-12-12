from django.test import SimpleTestCase
from ..forms import SignInForm
from unittest.mock import patch


class TestSignInForm(SimpleTestCase):
    @patch('signins.models.Student.is_student_signed_in', return_value=True)
    def test_name_must_be_unique_per_day(self, _patched_is_student_signed_in):
        '''
        A user should not be able to sign in twice per day.
        So, if a signin with that user exists for "today"
        the form should be invalid.
        '''
        form = SignInForm({'name': 'John Morgan'})

        is_valid = form.is_valid()

        _patched_is_student_signed_in.assert_called_once_with(
            name='John Morgan')
        self.assertFalse(is_valid)

    @patch('signins.models.Student.is_student_signed_in', return_value=False)
    def test_unsigned_in_student_is_valid(self, _patched_is_student_signed_in):
        '''
        A user who is not signed in should be valid.
        '''
        form = SignInForm({'name': 'John Morgan'})

        is_valid = form.is_valid()

        _patched_is_student_signed_in.assert_called_once_with(
            name='John Morgan')
        self.assertTrue(is_valid)
