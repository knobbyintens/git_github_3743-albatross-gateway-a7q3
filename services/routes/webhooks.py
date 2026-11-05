from services.gateway.decorators import gateway_route


@gateway_route(
    method="POST",
    path="/v1/webhooks/stripe",
    auth_required=False,
    status="stable",
    owner="integrations",
)
def stripe_webhook(request):
    return {"received": True}


@gateway_route(
    method="POST",
    path="/v1/webhooks/paypal",
    auth_required=False,
    status="stable",
    owner="integrations",
)
def paypal_webhook(request):
    return {"received": True}


@gateway_route(
    method="POST",
    path="/v1/webhooks/test",
    auth_required=False,
    status="deprecated",
    owner="integrations",
)
def test_webhook(request):
    return {"received": True}
