import os
from groq import Groq
from dotenv import load_dotenv
from cricket_scraper import get_live_scores
from news_api import get_cricket_news

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_cricket_response_stream(user_query, chat_history):

    live_scores = get_live_scores()
    news = get_cricket_news()

    system_prompt = f"""
You are a cricket assistant.

LIVE SCORES:
{live_scores}

LATEST NEWS:
{news}

Answer clearly and correctly.
"""

    messages = [{"role": "system", "content": system_prompt}]

    for role, msg in chat_history:
        messages.append({"role": role, "content": msg})

    messages.append({"role": "user", "content": user_query})

    try:
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",  
            messages=messages,
            temperature=0.3,
            max_tokens=500,
            stream=True,
        )

        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                yield content

    except Exception as e:
        yield f"Error: {str(e)}"