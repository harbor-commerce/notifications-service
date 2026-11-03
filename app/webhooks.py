from app import email

TEMPLATE_FOR = {"order.paid": "order_paid"}


def handle(event):
    template = TEMPLATE_FOR.get(event["type"])
    return email.render(template, order_id=event["id"]) if template else None
