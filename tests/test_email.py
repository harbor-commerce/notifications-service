import unittest

from app import email


class EmailTest(unittest.TestCase):
    def test_render(self):
        self.assertEqual(email.render("order_paid", order_id=7), "Your order 7 was paid.")
