# Day 4 — File Handling, Modes & Data Structuring (`os`, File Modes, `json`)

## Learning Resource

RAG Intern Learning Plan PDF — Week 1 (Day 4)

## Topics Learned

* **File Modes & Operations (File I/O)**
  * Modes Learned & Practiced:
    * Read (`'r'`): Reads existing content
    * Write (`'w'`): Creates new file or overwrites existing file
    * Append (`'a'`): Appends new data to the end of the file without deleting previous content
    * Read/Write (`'r+'`): Reads and overwrites from the beginning of the file
    * Append/Read (`'a+'`): Appends and reads content
  * Context Manager for automatic file closing (`with open(...) as f:`)
* **File Management with `os` Module**
  * Safe file deletion (`os.remove()`)
  * Checking file existence (`os.path.exists()`) to prevent runtime `FileNotFoundError`
* **Text Processing & Data Cleaning**
  * String replacing (`str.replace()`)
  * Whitespace stripping (`str.strip()`)
  * Parsing delimited lines (`str.split(",")`, `str.split("\n")`)
* **JSON & Data Structuring**
  * Basics of Python `json` module (`import json`, `json.dumps()`, `json.loads()`)
  * Structuring un-structured text records into Python Dictionaries (`dict`) and JSON format
  * Storing user objects inside a List of Dictionaries to prevent data overwriting

## Practical Work

* Created [`practice2.py`](file:///e:/Pyhton/DAY4/FileHandeling_Practice/practice2.py) — Practiced file modes (`'w'`, `'r+'`), file creation, string replacement ("Java" to "Python"), and keyword searching.
* Created [`practice3.py`](file:///e:/Pyhton/DAY4/FileHandeling_Practice/practice3.py) — Read raw data from [`p3.txt`](file:///e:/Pyhton/DAY4/FileHandeling_Practice/p3.txt), cleaned string tokens, and structured user records into a list of dictionaries/JSON objects.

## Timeline

* **22-08-2026 (Saturday):** Explored File Modes (`'r'`, `'w'`, `'a'`, `'r+'`, `'a+'`), file management using `os`, string cleaning, and initial exploration of JSON structuring.

## Project Progress

* **Text File to JSON Conversion:** Completed (Successfully converted raw text file into structured JSON/dictionary format).
* **PDF to JSON Conversion:** Next target (Partially complete / planned next).

## Status

**Day 4 — Partially Complete / Practical Done**
