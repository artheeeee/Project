import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from project.nonprofit.model_factories import BoxFactory, ClothFactory, EnvFactory

from .serializers import *


class DonationBoxSerialiserTest(APITestCase):
    box1 = None
    boxserializer = None

    def setUp(self):
        self.box1 = BoxFactory.create(pk=1, name="box1")
        self.boxserializer = BoxSerializer(instance=self.name)


    def test_donationboxSerilaiserHasCorrectFields(self):
        data = self.boxserializer.data
        self.assertEqual(set(data.keys()), set(['name', 'email',
                                                'phone', 'state', 'city',
                                                'address', 'sub_group']))

    def test_geneSerilaiserGeneIDIsHasCorrectData(self):
        data = self.boxserializer.data
        self.assertEqual(data['name'], "box1")

class DonationEnvSerialiserTest(APITestCase):
    env1 = None
    envserializer = None

    def setUp(self):
        self.box1 = EnvFactory.create(pk=1, name="env1")
        self.envserializer = EnvSerializer(instance=self.name)


    def test_donationenvSerilaiserHasCorrectFields(self):
        data = self.envserializer.data
        self.assertEqual(set(data.keys()), set(['name', 'email',
                                                'phone', 'state', 'city',
                                                'address', 'sub_group']))

    def test_envSerilaiserNameIsHasCorrectData(self):
        data = self.envserializer.data
        self.assertEqual(data['name'], "env1")

class ClothingSerialiserTest(APITestCase):
    cloth1 = None
    clothserializer = None

    def setUp(self):
        self.box1 = ClothFactory.create(pk=1, name="cloth1")
        self.boxserializer = ClothingSerializer(instance=self.cloth1)


    def test_clothingdonationSerilaiserHasCorrectFields(self):
        data = self.boxserializer.data
        self.assertEqual(set(data.keys()), set(['name', 'email',
                                                'phone', 'state', 'city',
                                                'address', 'sub_group', 'date', 'time']))

    def test_clothingSerilaiserNameIsHasCorrectData(self):
        data = self.boxserializer.data
        self.assertEqual(data['name'], "cloth1")
