from services.gateway.decorators import gateway_route


@gateway_route(
    method="GET",
    path="/v1/health",
    auth_required=False,
    status="stable",
    owner="platform-ops",
)
def health_check(request):
    return {"status": "ok"}


@gateway_route(
    method="GET",
    path="/v1/version",
    auth_required=False,
    status="stable",
    owner="platform-ops",
)
def version_info(request):
    return {"build": "4.1.3"}
