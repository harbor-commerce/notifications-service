TEMPLATES = {
    "order_paid": "Your order {order_id} was paid.",
}


def render(template, **values):
    return TEMPLATES[template].format(**values)


ROUTES = {"/templates": lambda: sorted(TEMPLATES)}
