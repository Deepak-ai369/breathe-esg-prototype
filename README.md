# ESG Ingestion Prototype

## Live Demo

Frontend:
https://breathe-esg-prototype-kappa.vercel.app/

Backend API:
https://breathe-esg-prototype-u1yw.onrender.com/api/records/

GitHub Repository:
https://github.com/Deepak-ai369/breathe-esg-prototype

---

## Overview

This project is a prototype ESG ingestion and review platform built using Django REST Framework and React.

The system supports:

* CSV-based ESG data ingestion
* Multi-tenant record structure
* Rule-based suspicious record detection
* Analyst approval workflow
* Audit locking after approval

---

## Tech Stack

Frontend:

* React
* Vite
* JavaScript

Backend:

* Django
* Django REST Framework
* Python

Database:

* SQLite

Deployment:

* Render
* Vercel

---

## Features

* Upload ESG CSV files
* Detect suspicious emission values
* Flag records for analyst review
* Approve records
* Lock approved records
* Multi-tenant structure

---

## Architecture

React Frontend
↓
Django REST API
↓
SQLite Database

---

## Tradeoffs

* CSV ingestion instead of direct SAP integration
* Rule-based validation instead of ML anomaly detection
* SQLite used for prototype simplicity
* Synchronous ingestion used for rapid delivery

---

## Future Improvements

* PostgreSQL support
* Async ingestion pipeline
* Tenant-specific validation rules
* Authentication and RBAC
* Audit history tracking
