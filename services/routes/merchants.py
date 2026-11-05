from services.gateway.decorators import gateway_route


@gateway_route(
    method="POST",
    path="/v1/merchants",
    auth_required=True,
    status="beta",
    owner="merchant-success",
)
def create_merchant(request):
    return {"merchant_id": "m_new"}


@gateway_route(
    method="GET",
    path="/v1/merchants",
    auth_required=True,
    status="stable",
    owner="merchant-success",
)
def list_merchants(request):
    return {"items": []}
