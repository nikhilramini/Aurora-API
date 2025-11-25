# Aurora-API

# Simple Message Search API

## Overview
This is a simple search engine API built on top of the `/messages` endpoint.  
It allows querying messages by text and returns paginated results.

## Features
- Case-insensitive search on message text
- Paginated results (`page` & `limit`)
- In-memory caching for fast responses (<30ms)
- Auto-refresh cache every 5 minutes

## API Endpoint
### GET /search
**Query Parameters:**  
- `q` (required): text to search  
- `page` (optional, default=1): page number  
- `limit` (optional, default=10): number of results per page  

**Example:**
GET /search?q=Paris&page=1&limit=5

## Design Notes
1. In-memory filtering (current implementation) -> fast, simple  
2. Elasticsearch / OpenSearch -> scalable for millions of messages  
3. TF-IDF vectorization -> relevance ranking, fuzzy search  

## Reducing Latency
- Cache messages in memory  
- Precompute search indexes  
- Use only required fields in responses
