# 🧠 Wikipedia Random Fact Fetcher

This is a simple Python script that fetches a random Wikipedia article summary using the [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/). It displays the article's title, a short summary, and a link to the full article.

## 🚀 Features

- Fetches a random fact from Wikipedia every time you run it
- Displays:
  - ✅ Title of the article
  - ✅ Short summary (extract)
  - ✅ Link to the full Wikipedia page
- Handles missing data safely using `.get()` for nested dictionaries

## 🛠️ Tech Stack

- 🐍 Python 3
- 📡 Wikipedia REST API
- 📦 `requests` library for HTTP calls

## 📦 Requirements

Install the `requests` library if you don't have it:

```bash
pip install requests
