from django.test import TestCase


class TwoPlusTwo(TestCase):

    def test_1(self):
        self.assertEqual(2+2, 4)
