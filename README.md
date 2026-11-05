# Albatross Pay Gateway

Payment routing and settlement gateway for Albatross Pay merchant traffic.

The service exposes versioned HTTP routes under `services/routes/`. Each handler
declares its routing metadata with the `gateway_route` decorator.

Operational documentation for a release cut is published together with the code
that ships in that cut.
