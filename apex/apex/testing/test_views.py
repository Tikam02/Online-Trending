from django.test import SimpleTestCase
from django.urls import reverse
from apex.apps.services.views import *

class feedback_page_test(SimpleTestCase):

    def test_feedback_page(self):
            response = self.client.get(reverse('feedback'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'feedback.html')


    def test_about_page_status_code(self):
        response = self.client.get('/feedback', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')


    def test__page_does_not_contain_incorrect_html(self):
        response = self.client.get('/feedback', follow=True)
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

class login_page_test(SimpleTestCase):
    def test_search_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        def test_login_page(self):
            response = self.client.get('/login', follow=True)
            self.assertEqual(response.status_code, 200)

        def login_view_url_by_name(self):
            response = self.client.get(reverse('login'))
            self.assertEqual(response.status_code, 200)


        def test_login__page_does_not_contain_incorrect_html(self):
            response = self.client.get('/login', follow=True)
            self.assertNotContains(
                response, 'Hi there! I should not be on the page.')

class Sign_up_page_test(SimpleTestCase):
    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_status_code(self):
        response = self.client.get('/signup', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test__signup_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/signup', follow=True)
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

#
# class Search_page_test(SimpleTestCase):
#
#     def test_search_page(self):
#         response = self.client.get(reverse('/search'))
#         self.assertEqual(response.status_code, 200)
