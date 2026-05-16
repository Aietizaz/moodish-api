# Moodish

Moodish is a backend-first meal recommendation API built with Python and FastAPI. It recommends meals from a small catalogue using deterministic ranking logic based on mood, effort level, dietary preferences, and available preparation time.

This project is designed as a portfolio backend to demonstrate practical API engineering skills rather than frontend polish. The emphasis is on request validation, clean separation of concerns, explainable recommendation logic, and automated testing.

## Why This Project

- FastAPI route design and request handling
- Pydantic schema validation
- service-layer business logic
- deterministic recommendation scoring
- testable architecture
- automated API and service tests
- clean project structure for future extension
- fun project based on cooking, recipes and food which is a personal interest and relatable

The current implementation is intentionally a focused MVP. It aims to show a complete backend slice that can be iterated into a more production-style service.

## Current Features

- `GET /health` health-check endpoint
- `GET /meals` endpoint for listing available meals
- `POST /recommendations` endpoint for ranked meal recommendations
- deterministic scoring based on:
  - mood match
  - effort match
  - preparation time fit
  - dietary tag match
- top 3 recommendations returned with an explanation for each result
- in-memory meal seed data loaded from JSON
- automated tests with `pytest`

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest

## Architecture

The codebase is structured to separate HTTP concerns from application logic:

```text
app/
├── api/
│   └── routes/
│       ├── health.py
│       ├── meals.py
│       └── recommendations.py
├── db/
│   ├── meals.json
│   └── seed.py
├── schemas/
│   ├── meals.py
│   └── recommendations.py
├── services/
│   ├── meal_service.py
│   └── recommendation_service.py
└── main.py

tests/
├── test_health.py
├── test_meals.py
└── test_recommendations.py
```

### Design Notes

- `routes` define the API surface
- `schemas` define validated request and response contracts
- `services` hold business logic outside the HTTP layer
- `db/meals.json` provides simple seed data for the MVP

This structure is intended to scale into a more production-ready backend with persistence, configuration, and infrastructure concerns added later.

## API Endpoints

### `GET /health`

Simple health check used to confirm the API is running.

Example response:

```json
{
  "status": "ok"
}
```

### `GET /meals`

Returns the available meals in the current catalogue.

Example response:

```json
[
  {
    "id": 1,
    "name": "Chicken Rice Bowl",
    "preparation_time_mins": 15,
    "effort": "low",
    "dietary_tags": ["high_protein"],
    "mood_tags": ["tired", "focused"],
    "protein_rating": 7,
    "comfort_rating": 4,
    "ingredients": ["chicken", "rice", "soy sauce"]
  }
]
```

### `POST /recommendations`

Returns the top 3 ranked recommendations for a given set of user preferences.

Example request:

```json
{
  "mood": "tired",
  "dietary_tags": ["high_protein"],
  "effort": "low",
  "preparation_time_mins": 15
}
```

Example response:

```json
{
  "recommendations": [
    {
      "meal_name": "Chicken Rice Bowl",
      "score": 10.0,
      "reason": "It matches your current mood (tired). It requires (low) effort. It can be prepared within your requested time limit (15 mins). It matches your dietary preferences (high_protein)."
    },
    {
      "meal_name": "Quinoa Salad",
      "score": 5.0,
      "reason": "It requires (low) effort. It can be prepared within your requested time limit (15 mins)."
    },
    {
      "meal_name": "Grilled Salmon with Veggies",
      "score": 2.5,
      "reason": "It matches your dietary preferences (high_protein)."
    }
  ]
}
```

## Recommendation Logic

The recommendation engine is intentionally deterministic and explainable.

For each meal, the service assigns points for matching:

- mood
- effort level
- preparation time constraint
- dietary tags

Meals are then sorted by score, and the top 3 are returned along with a generated explanation describing why each meal was recommended.

This approach keeps the MVP transparent and easy to test while leaving room for more advanced ranking strategies later.

## Running Locally

From the project root:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
py -m uvicorn app.main:app --reload --port 9999
```

Interactive API docs:

```text
http://127.0.0.1:9999/docs
```

## Running Tests

```bash
py -m pytest
```

## Current Status

This repository currently represents a Phase 1 backend MVP:

- functional FastAPI application
- validated request and response models
- deterministic recommendation service
- automated test coverage for core endpoints

The current implementation uses JSON seed data rather than a real database and focuses on the backend core before infrastructure and deployment polish.

## Roadmap

Planned next steps for expanding Moodish into a more production-style backend:

### Backend and Data

- move from JSON seed data to PostgreSQL persistence
- introduce SQLAlchemy models and migrations
- store recommendation history
- support user preferences and favourites

### Engineering Polish

- improve test coverage
- add structured logging and configuration management
- add Docker support for local development
- add GitHub Actions CI

### Optional AI Layer

AI is intended as an enhancement layer, not the core recommendation system.

Potential future uses:

- generate more natural recommendation explanations
- parse messy free-text user inputs into structured fields
- suggest meal substitutions
- build weekly meal plans from deterministic recommendation results

The deterministic recommendation engine should remain fully functional even without AI.

## What This Project Demonstrates

Even in MVP form, Moodish is intended to show:

- backend-first product thinking
- API design with clear schemas
- separation between routing and business logic
- explainable decision-making in application code
- test-driven iteration on backend behavior

## Author Notes

This project is being built incrementally as a learning-focused backend portfolio piece. The goal is not to over-engineer early, but to build a clean foundation and then extend it with stronger infrastructure and persistence over time.
