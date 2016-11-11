from django.test import TestCase

# Create your tests here.


def test_home_page_status_code_is_ok(self):
    home_page = self.client.get('/')
    self.assertEquals(home_page.status_code, 200)