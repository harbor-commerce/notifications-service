TEMPLATES = {
    "order_paid": "Your order {order_id} was paid.",
    "order_shipped": "Your order {order_id} is on its way.",
    "refund_issued": "We refunded {amount} for order {order_id}.",
}


def render(template, **values):
    return TEMPLATES[template].format(**values)


ROUTES = {"/templates": lambda: sorted(TEMPLATES)}
