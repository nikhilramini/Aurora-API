# Simple Message Search API

## Public Deployment
The API is deployed publicly at:  
**[https://aurora-api-phf1.onrender.com](https://aurora-api-phf1.onrender.com)**  
Swagger docs: [https://aurora-api-phf1.onrender.com/docs](https://aurora-api-phf1.onrender.com/docs)

### Example API Calls
- Search for "Paris": q=Paris, page=1, limit=5
https://aurora-api-phf1.onrender.com/search?q=Paris&page=1&limit=5


### Local Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run locally:
```bash
pip install -r requirements.txt
```
4. Open Swagger docs:
```bash
http://127.0.0.1:8000/docs
```
Overview

This is a simple search engine API built on top of the /messages endpoint.
It allows querying messages by text and returns paginated results.

The API is designed for fast, case-insensitive search with caching for low-latency responses.

Features

Case-insensitive search on message text

Paginated results using page and limit parameters

In-memory caching for fast responses (<30ms)

Auto-refresh cache every 5 minutes

Optional endpoints for cache management (if implemented):

/cache-status → check current cache size

/update-cache → manually refresh cache

API Endpoint
GET /search

Search messages containing a query string and return paginated results.

Query Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q`       | string | Yes | Text to search for (case-insensitive) |
| `page`    | int    | No  | Page number (default: 1) |
| `limit`   | int    | No  | Number of results per page (default: 10) |
