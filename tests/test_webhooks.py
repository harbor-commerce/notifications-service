import unittest

from app import webhooks


class WebhooksTest(unittest.TestCase):
    def test_paid(self):
        self.assertEqual(webhooks.handle({"type": "order.paid", "id": 3}), "Your order 3 was paid.")

    def test_unknown(self):
        self.assertIsNone(webhooks.handle({"type": "order.created", "id": 3}))
