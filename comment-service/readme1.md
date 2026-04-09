# Comment Service (Microservice)

## Overview

This is a standalone Comment Service designed as part of the IT Helpdesk system. It is responsible for handling all comment-related operations independently from the main application, extracted from the monolithic architecture to simulate a microservices-based design.

---

## Features

- Add comments to a ticket
- Retrieve comments for a specific ticket
- Independent service with its own database

---

## Architecture

This service is a lightweight Flask-based microservice with the following components: a Flask API layer, an SQLite database (`comments.db`), and REST endpoints.

---

## API Endpoints

### Get Comments for a Ticket

```
GET /comments/<ticket_id>
```

**Response:**
```json
[
  {
    "id": 1,
    "ticket_id": 1,
    "comment": "Checking this issue",
    "created_at": "2026-01-01 10:00:00"
  }
]
```

### Add a Comment to a Ticket

```
POST /comments/<ticket_id>
```

**Request body:**
```json
{
  "comment": "Issue is being investigated"
}
```

---

## Architectural Design Decisions

### Monolith Extraction

Comment functionality was decoupled from the main monolith to promote modularity and allow the service to scale independently of the main application.

### Communication Layer

REST APIs were implemented for all inter-service communication, ensuring a standard, language-agnostic way for the main service to interact with comment data.

### Database Selection

SQLite was chosen as the primary data store, prioritizing simplicity and rapid setup for the initial deployment phase.

### Service Philosophy

The service maintains a lightweight and independent footprint to minimize overhead and ensure it can be easily containerized or moved without heavy dependency chains.
