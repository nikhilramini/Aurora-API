# Simple Message Search API

## Overview
This is a simple search engine API built on top of the `/messages` endpoint.  
It allows querying messages by text and returns **paginated results**.  

The API is designed for **fast, case-insensitive search** with caching for low-latency responses.

---

## Features
- **Case-insensitive search** on message text
- **Paginated results** using `page` and `limit` parameters
- **In-memory caching** for fast responses (<30ms)
- **Auto-refresh cache** every 5 minutes
- Optional endpoints for cache management (if implemented):
  - `/cache-status` → check current cache size
  - `/update-cache` → manually refresh cache

---

## API Endpoint

### **GET /search**
Search messages containing a query string and return paginated results.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q`       | string | Yes | Text to search for (case-insensitive) |
| `page`    | int    | No  | Page number (default: 1) |
| `limit`   | int    | No  | Number of results per page (default: 10) |

**Example Request:**
```http
GET /search?q=Paris&page=1&limit=5

- Precompute search indexes  
- Use only required fields in responses
