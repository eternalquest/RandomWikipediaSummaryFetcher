
# 🧠 Random Wikipedia Summary Fetcher

A simple and interactive Python GUI application that fetches and displays random Wikipedia article summaries along with their images using the [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/). Built using `tkinter`, `Pillow`, and `requests`, this app lets you explore interesting random topics and read more directly in your browser.

## 📸 Features

* Fetches a random Wikipedia article title, summary, and image.
* Displays article content in a user-friendly full-screen window.
* "New Article" button to refresh and get a new fact.
* "Read More" button to open the full article in your default web browser.
* Handles missing images gracefully.

## 🛠️ Requirements

* Python 3.x
* Required Python packages:

  * `requests`
  * `Pillow`

You can install the dependencies using:

```bash
pip install requests pillow
```

## ▶️ How to Run

1. Save the script to a file, e.g., `wikipedia_gui.py`.
2. Run the script:

```bash
python mainGuitkinter.py
```

## 🧩 How It Works

* It uses the `/page/random/summary` endpoint from Wikipedia REST API to get a random article.
* The GUI is built with `tkinter` and dynamically updates the title, summary, and image.
* Image loading includes headers to avoid forbidden errors.
* Buttons let the user refresh for a new fact or open the full article in a browser.

## 📷 Example Output

* Title: *Ada Lovelace*
* Summary: *Augusta Ada King, Countess of Lovelace was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer...*
* Image: Displayed if available
* Buttons:

  * 🆕 New Article
  * 🔗 Read More

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).


