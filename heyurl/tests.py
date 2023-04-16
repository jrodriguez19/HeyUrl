from django.test import TestCase
from django.urls import reverse, resolve
from .models import Url

class IndexTests(TestCase):
    def test_no_urls(self):
        """
        If no URLs exist, an appropriate message is displayed
        """
        # response = self.client.get(reverse('index'))

    def test_submitting_new_url_failure(self):
        """
        When submitting an invalid URL, an error is returned to the user
        """
        #response = self.client.get(reverse('store'))

    def test_submitting_new_url_success(self):
        """
        When submitting a valid URL, a success message is displayed
        """
        #response = self.client.get(reverse('store'))

    def test_visiting_short_url_missing(self):
        """
        If short URL does not exist, custom 404 page is displayed
        """
        # response = self.client.get(reverse('u/dne'))


    def test_visiting_short_url(self):
        """
        If short URL exists, stats logged and redirected to original URL
        """
        #response = self.client.get(reverse('u/dne'))
        
