# Tradeoffs and Design Decisions

## CSV Ingestion Instead of SAP Integration

Direct SAP integration would require enterprise connectors and authentication workflows.

CSV ingestion was chosen because CSV exports are common in ESG operational reporting and allowed faster prototype delivery.

---

## Rule-Based Validation Instead of ML

The system uses deterministic threshold-based suspicious record detection.

Advantages:

* Explainable
* Auditable
* Easy to validate
* Faster to implement

Machine learning anomaly detection was intentionally avoided due to prototype scope and limited training data.

---

## SQLite Instead of PostgreSQL

SQLite was selected for simplicity and rapid development.

Advantages:

* Zero configuration
* Lightweight
* Easy local setup

For production systems, PostgreSQL would be preferred for scalability and concurrency.

---

## Synchronous Processing

CSV ingestion currently runs synchronously inside API requests.

Advantages:

* Simpler architecture
* Faster implementation

Future versions should move ingestion into asynchronous background jobs using Celery or message queues.

---

## No Authentication Layer

Authentication and RBAC were intentionally excluded to prioritize core ingestion workflow delivery within limited implementation time.
