from services.gateway.decorators import gateway_route


@gateway_route(
    method="GET",
    path="/v1/internal/routing-table",
    auth_required=False,
    status="stable",
    owner="gateway-platform",
)
def routing_table(request):
    return {"routes": []}


@gateway_route(
    method="POST",
    path="/v1/internal/route-reload",
    auth_required=False,
    status="stable",
    owner="gateway-platform",
)
def route_reload(request):
    return {"reloaded": True}
