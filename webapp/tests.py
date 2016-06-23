from django.test import TestCase

# Create your tests here.
class HomePageViewTestCase(TestCase):

    def test_daycamp(self):
        response = self.client.get('/')
        self.assertContains(response, 'DayCamp!', status_code=200)
