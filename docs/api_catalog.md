# Albatross Pay Gateway — endpoint notes

Personal scratch notes used while reviewing the gateway surface. Not the
published catalog; kept only for quick grepping.

- `GET /v1/health` -> platform-ops (open)
- `GET /v1/version` -> platform-ops (open)
- `POST /v1/payments` -> payments-core (token required)
- `GET /v1/payments` -> payments-core (token required)
- `DELETE /v1/payments/{payment_id}` -> payments-core (old, retired)
- `POST /v1/payments/{payment_id}/refunds` -> payments-core (token required)
- `GET /v1/refunds` -> payments-core (beta)
- `POST /v1/payouts` -> payouts (token required)
- `GET /v1/payouts` -> payouts (token required)
- `POST /v1/webhooks/stripe` -> integrations (signature checked)
- `POST /v1/webhooks/paypal` -> integrations (signature checked)
- `GET /v1/internal/routing-table` -> gateway-platform (internal only)
- `POST /v1/merchants` -> merchant-success (beta)
- `GET /v1/merchants` -> merchant-success (token required)
