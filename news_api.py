import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_cricket_news():
    url = f"https://newsapi.org/v2/everything?q=cricket&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"

    try:
        res = requests.get(url)
        articles = res.json().get("articles", [])
        return "\n".join([f"- {a['title']}" for a in articles[:5]])

    except Exception as e:
        return f"Error fetching news: {str(e)}"