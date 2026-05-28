# Data Model Design

## Tenant

Represents an organization using the ESG platform.

Fields:

* name

Purpose:
Supports multi-tenant SaaS architecture where multiple companies can store ESG records independently.

---

## EmissionRecord

Represents a normalized ESG emission entry.

Fields:

* tenant
* activity_type
* quantity
* unit
* status
* is_suspicious
* created_at

Purpose:
Stores ingested operational ESG activity records.

---

## Workflow Logic

Initial State:

* PENDING

If suspicious thresholds exceeded:

* FLAGGED

After analyst approval:

* APPROVED

Approved records become locked from further modification.

---

## Relationships

One Tenant
→ Many EmissionRecords

This supports organizational separation and scalability for future multi-company support.
