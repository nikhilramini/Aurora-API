from fastapi import FastAPI, Query
from typing import List
import requests
import threading
import time

app = FastAPI(title="Simple Message Search API")

BASE_URL = "https://november7-730026606190.europe-west1.run.app/messages"
CACHE_REFRESH_INTERVAL = 300  # seconds (5 minutes)

# In-memory cache
message_cache = []
cache_last_updated = 0
cache_lock = threading.Lock()


def update_cache():
    """Fetch all messages from external API and store in memory"""
    global message_cache, cache_last_updated
    skip = 0
    limit = 100
    all_messages = []

    while True:
        try:
            response = requests.get(BASE_URL, params={"skip": skip, "limit": limit}, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching messages: {e}")
            break

        data = response.json()
        items = data.get("items", [])
        if not items:
            break

        all_messages.extend(items)
        skip += limit

    with cache_lock:
        message_cache = all_messages
        cache_last_updated = time.time()
    print(f"Cache updated with {len(all_messages)} messages.")


@app.on_event("startup")
def startup_event():
    # Populate cache on startup
    update_cache()

    # Background thread to refresh cache periodically
    def refresh_loop():
        while True:
            time.sleep(CACHE_REFRESH_INTERVAL)
            update_cache()

    thread = threading.Thread(target=refresh_loop, daemon=True)
    thread.start()


@app.get("/search")
def search_messages(
    q: str = Query(..., min_length=1, description="Text to search for"),
    page: int = Query(1, description="Page number"),
    limit: int = Query(10, description="Number of results per page")
):
    """
    Search messages containing 'q' (case-insensitive) and return paginated results
    """
    with cache_lock:
        messages = message_cache.copy()

    # Filter messages by query
    matching = [msg for msg in messages if q.lower() in msg.get("message", "").lower()]

    # Paginate results
    start = (page - 1) * limit
    end = start + limit
    paginated = matching[start:end]

    return {
        "total_matches": len(matching),
        "page": page,
        "limit": limit,
        "results": paginated
    }


@app.get("/cache-status")
def cache_status():
    """Check how many messages are currently cached"""
    with cache_lock:
        return {"cached_messages": len(message_cache)}
