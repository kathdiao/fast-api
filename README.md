# Fast API

A beginner-friendly FastAPI project for personal learning and practice for testing and backend development.  
This project focuses on understanding API development, routes, HTTP methods, and status codes.

## Description
This repository contains practice projects using FastAPI to understand:

- Path parameters
- Query parameters
- HTTP methods: GET, POST, PUT, DELETE
- HTTP status codes (200, 201, 204, 400, 401, 403, 404, 409, 422, 500)
- Basic API testing using Swagger UI (/docs)
- Backend development concepts 

## HTTP Methods Overview
| Method | Description |
|--------|-------------|
| GET    | Retrieve information |
| POST   | Add new information |
| PUT    | Update existing information |
| DELETE | Remove information |

## Common HTTP Status Codes
| Code | Meaning |
|------|---------|
| 200  | OK (success) |
| 201  | Created |
| 204  | No Content |
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 409  | Conflict |
| 422  | Unprocessable Entity |
| 500  | Internal Server Error |

## How to Run
1. Install dependencies:
pip install fastapi uvicorn

2. Run the server:
uvicorn working:app --reload

3. Open browser to test:
- API endpoint: `http://127.0.0.1:8000/`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Notes
- This is a **personal learning and practice project** for FastAPI, testing, and backend development.
- All routes are simple and self-contained.
- Swagger UI automatically documents all routes and parameters.
