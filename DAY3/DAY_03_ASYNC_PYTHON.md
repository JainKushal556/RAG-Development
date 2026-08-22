# Day 3 — Asynchronous Programming (`async`, `await`, `httpx` & `venv`)

## Learning Resource

RAG Intern Learning Plan PDF — Week 1 (Day 3)

## Topics Learned

* **Virtual Environment (`venv`)**
  * Creating `.venv` (`python -m venv .venv`)
  * Activating environment & installing `httpx` (`pip install httpx`)
* **Asynchronous Programming (`asyncio`)**
  * Sync vs Async (Non-blocking I/O)
  * `async def` (Defining Coroutines)
  * `await` keyword (Pausing execution without blocking event loop)
  * `asyncio.run()` (Launching the Event Loop)
* **Async HTTP Client (`httpx`)**
  * Why `httpx` over `requests` for async tasks
  * Using async context manager (`async with httpx.AsyncClient() as client:`)
* **Key Debugging Concepts Learned**
  * Must use parentheses `()` when instantiating `httpx.AsyncClient()`
  * Must explicitly `return` values from coroutines to avoid getting `None`
  * Iterating and printing dictionary keys and values (`fetched_data[key]`)

## Practical Work

* Created virtual environment `.venv` and installed `httpx`.
* Built async API data fetcher (`async.py`) using `httpx` and `asyncio` to pull user-requested records from JSONPlaceholder API.

## Timeline

* **20-08-2026 & 21-08-2026 (Thursday & Friday):** Read and understood the theoretical concepts of Async/Await, Event Loop, and non-blocking I/O.
* **22-08-2026 (Saturday):** Completed Day 3 practical work, setup `.venv`, wrote `async.py`, debugged runtime issues, and verified output.

## Status

**Day 3 — Completed**
