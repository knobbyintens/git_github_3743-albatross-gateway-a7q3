from services.gateway.decorators import gateway_route


@gateway_route(
    method="POST",
    path="/v1/payments",
    auth_required=True,
    status="stable",
    owner="payments-core",
)
def create_payment(request):
    return {"payment_id": "pay_new"}


@gateway_route(
    method="GET",
    path="/v1/payments",
    auth_required=True,
    status="stable",
    owner="payments-core",
)
def list_payments(request):
    return {"items": []}


@gateway_route(
    method="DELETE",
    path="/v1/payments/{payment_id}",
    auth_required=True,
    status="deprecated",
    owner="payments-core",
)
def delete_payment(request):
    raise NotImplementedError("retired in the 4.2 cut")
