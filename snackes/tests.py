
from django.test import SimpleTestCase

from django.urls import reverse
# Create your tests here.

class snacksTest(SimpleTestCase):
    def test_snack_status_code(self):
        url=reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_snack_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
