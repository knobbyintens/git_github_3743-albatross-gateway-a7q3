from services.gateway.decorators import gateway_route


@gateway_route(
    method="GET",
    path="/v1/public/status",
    auth_required=False,
    status="stable",
    owner="platform-ops",
)
def public_status(request):
    return {"state": "operational"}
