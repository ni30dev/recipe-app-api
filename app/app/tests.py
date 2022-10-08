from django.test import SimpleTestCase

from app import calc


class calcTest(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(5, 7)

        self.assertEqual(res, 12)
