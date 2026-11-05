from services.gateway.decorators import gateway_route


@gateway_route(
    method="POST",
    path="/v1/payments/{payment_id}/refunds",
    auth_required=True,
    status="stable",
    owner="payments-core",
)
def create_refund(request):
    return {"refund_id": "ref_new"}


@gateway_route(
    method="GET",
    path="/v1/refunds",
    auth_required=True,
    status="beta",
    owner="payments-core",
)
def list_refunds(request):
    return {"items": []}


@gateway_route(
    method="DELETE",
    path="/v1/refunds/{refund_id}",
    auth_required=True,
    status="deprecated",
    owner="payments-core",
)
def cancel_refund(request):
    raise NotImplementedError("retired in the 4.2 cut")
