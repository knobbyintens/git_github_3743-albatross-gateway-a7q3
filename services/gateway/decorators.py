"""Route declaration helpers for the Albatross Pay gateway."""


def gateway_route(
    method,
    path,
    auth_required=False,
    status="stable",
    owner="gateway-platform",
):
    """Attach routing metadata to a handler function."""

    def decorator(func):
        func.route_meta = {
            "method": method,
            "path": path,
            "auth_required": auth_required,
            "status": status,
            "owner": owner,
        }
        return func

    return decorator
