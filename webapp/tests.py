from django.test import TestCase

# Create your tests here.
def test_daycamp(self):
    response = self.client.get('/')
    self.assertContains(response, 'DayCamp!', status_code=200)
