# Albatross Pay — API Catalog

Maintained for the active release cut. Values mirror the route metadata declared
under `services/routes/`.

## Gateway Route Catalog

| Method | Path | Exposure | Owner | Status |
| --- | --- | --- | --- | --- |
| POST | /v1/payments | Restricted | payments-core | stable |
| GET | /v1/health | Public | platform-ops | stable |
| DELETE | /v1/payments/{payment_id} | Restricted | payments-core | deprecated |
| GET | /v1/payments | Restricted | payments-core | stable |
| GET | /v1/version | Public | platform-ops | stable |

## Notes

`Exposure` is derived from route authentication and reserved internal path
prefixes. Deprecated routes are not carried into the published catalog.
