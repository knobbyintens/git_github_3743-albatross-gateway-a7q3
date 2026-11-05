from services.gateway.decorators import gateway_route


@gateway_route(
    method="POST",
    path="/v1/payouts",
    auth_required=True,
    status="stable",
    owner="payouts",
)
def create_payout(request):
    return {"payout_id": "po_new"}


@gateway_route(
    method="GET",
    path="/v1/payouts",
    auth_required=True,
    status="stable",
    owner="payouts",
)
def list_payouts(request):
    return {"items": []}
