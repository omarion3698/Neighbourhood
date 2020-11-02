from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Kibra = neighbourhood(neighbourhood='Kibra')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kibra,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Kibra.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kibra.delete_neighbourhood('Kibra')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class HealthservicesTestClass(TestCase):
    def setUp(self):
        self.Sugery = healthservices(healthservices='Surgery')

    def test_instance(self):
        self.assertTrue(isinstance(self.Surgery,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Surgery.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Surgery.delete_healthservices('Surgery')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)