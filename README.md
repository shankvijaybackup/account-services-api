# account-services-api

AtomBank Account Services — FastAPI microservice for account balance, transaction history and customer data.

## Stack
Python 3.12 · FastAPI · SQLAlchemy · PostgreSQL · Flyway

[![Build](https://dev.azure.com/AtomicworkBanking/AtomBanking/_apis/build/status/account-services-api)](https://dev.azure.com/AtomicworkBanking/AtomBanking/_build)

## Endpoints
- `GET  /accounts/{id}/balance` — Real-time balance
- `GET  /accounts/{id}/transactions` — Transaction history
- `POST /accounts/{id}/freeze` — Freeze account
- `GET  /health` — Health check