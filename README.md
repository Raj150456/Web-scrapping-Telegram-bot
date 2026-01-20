# Web-scrapping-Telegram-bot

Project Title
Web-scrapping-Telegram-bot — a small Python bot that fetches RSS feed items and posts them to a Telegram group.

Overview

- Learning goal: Practice working with web data (RSS), parsing feeds, and using Telegram Bot API for automated posting.
- What it does: Polls BBC RSS feed and posts the latest items (title, short summary, link) to a Telegram group when requested.

Key Features

- Fetches RSS feeds and parses entries
- Command to request news: `/dailynews` for BBC News
- Posts title, short description, and link to a Telegram chat
- Runs as a simple script that polls and responds to commands

Tech Stack (only what exists in the repo)

- Python
- Libraries used: requests, feedparser (uses direct HTTP requests to Telegram Bot API)

How to run locally

1. Clone the repo:
   git clone https://github.com/Raj150456/Web-scrapping-Telegram-bot.git
2. Create a Python virtual environment and activate it (recommended):
   python3 -m venv venv
   source venv/bin/activate # Linux / macOS
   venv\Scripts\activate # Windows
3. Install dependencies:
   pip install requests feedparser
4. Configure environment variables (example):
   - TELEGRAM_BOT_TOKEN (your bot token)
   - TELEGRAM_CHAT_ID (target chat or group id)
     You can export these or put them in a `.env` file and load them in the script.
5. Run the bot:
   python Bot1.py

What I learned

- How RSS feeds are structured and how to parse them with feedparser
- How to call external APIs from Python and post messages to Telegram
- How to run and test simple automation scripts locally
