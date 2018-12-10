from .functional_testcase import FunctionalTestCase


class TestSignIn(FunctionalTestCase):
    '''
    A student should be able to:
    - go to the home page
    - see (and click) a link for signing in
    - fill out the sign in form
    - see themselves as signed in
    '''

    def test_happy_path(self):
        self.browser.visit('/')

        self.browser.click_link_by_partial_text('Sign In')

        self.browser.fill_form(
            {
                'name': 'Alyssa P. Hacker'
            },
            form_id='sign-in-form',
        )
        self.browser.find_by_css('#sign-in-form button').first.click()

        signed_in_students = self.browser.find_by_id(
            'signed-in-students').first

        self.assertIn('Alyssa P. Hacker', signed_in_students.text)
