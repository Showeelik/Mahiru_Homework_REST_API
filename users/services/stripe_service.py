import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_product(course):
    """
    Создает продукт в Stripe.
    """
    product = stripe.Product.create(name=course.name, description=course.description)
    return product["id"]


def create_stripe_price(product_id, amount):
    """
    Создает цену в Stripe.
    """
    price = stripe.Price.create(
        product=product_id,
        unit_amount=int(amount * 100),  # цена в копейках
        currency="usd",
    )
    return price["id"]


def create_checkout_session(price_id, success_url, cancel_url):
    """
    Создает сессию для оплаты в Stripe.
    """
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": price_id,
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session["url"]


def get_payment_status(session_id):
    """
    Проверяет статус платежа.
    """
    session = stripe.checkout.Session.retrieve(session_id)
    return session.get("payment_status")
