import requests
import feedparser

# Your bot token
BOT_TOKEN = "Your Bot Token"
# Your group chat ID
CHAT_ID = "Your Group Chat ID"

# Function to send a message to the Telegram group
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Failed to send message: {response.status_code}, {response.text}")

# Fetch the latest news from BBC
def fetch_bbc_news():
    # BBC News RSS feed URL
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(feed_url)
    
    articles = []
    # Get the top 5 latest articles from the BBC feed
    for entry in feed.entries[:5]:
        title = entry.title
        summary = entry.summary
        link = entry.link
        
        # Construct a short article string
        article = f"{title}\n{summary}\nRead more: {link}"
        articles.append(article)
    
    return "\n\n".join(articles)

# Main function to listen and handle /dailynews commands
def handle_commands():
    print("Bot is running...")
    while True:
        updates = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates").json()
        for update in updates.get("result", []):
            if "message" in update and "text" in update["message"]:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"]["text"]
                
                # Check if the command is /dailynews and matches the group
                if text.lower() == "/dailynews" and str(chat_id) == CHAT_ID:
                    news = fetch_bbc_news()
                    send_message(news)
                    
        # Send an offset to Telegram to avoid processing the same updates repeatedly
        if updates.get("result"):
            last_update_id = updates["result"][-1]["update_id"] + 1
            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates", params={"offset": last_update_id})

# Run the bot
if __name__ == "__main__":
    handle_commands()