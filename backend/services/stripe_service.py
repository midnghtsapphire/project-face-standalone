import os
import stripe
from typing import Optional

class StripeService:
    def __init__(self):
        self.mode = os.getenv("STRIPE_MODE", "test").lower()
        if self.mode == "live":
            self.secret_key = os.getenv("STRIPE_LIVE_SECRET_KEY")
            self.publishable_key = os.getenv("STRIPE_LIVE_PUBLISHABLE_KEY")
        else:
            self.secret_key = os.getenv("STRIPE_TEST_SECRET_KEY")
            self.publishable_key = os.getenv("STRIPE_TEST_PUBLISHABLE_KEY")
        
        stripe.api_key = self.secret_key

    def get_publishable_key(self):
        return self.publishable_key

    async def create_checkout_session(self, customer_email, price_id, success_url, cancel_url):
        return stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price': price_id, 'quantity': 1}],
            mode='subscription',
            customer_email=customer_email,
            success_url=success_url,
            cancel_url=cancel_url,
        )
