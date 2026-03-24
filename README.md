Project Title : Cricket Live Chatbot

Description: 

This is a cricket chatbot genearted using LLM. 
It provides match insights, cricket news, and interactive responses using LLMs.

The chatbot integrates live cricket scores (via web scraping) and news APIs to generate accurate and engaging responses.



Features

ChatGPT-like interface
Fast responses using Groq LLM
cricket score integration
Latest cricket news (NewsAPI)
Real-time streaming responses

Tech Stack

- Python
- Streamlit
- Groq API (LLM)
- BeautifulSoup (Web scraping)
- NewsAPI


Project Structure

app.py              # Streamlit UI
chatbot.py          # LLM logic (Groq)
cricket_scraper.py  # Live score scraping
news_api.py         # News fetching


Setup Instructions

1. Clone the repository:
   git clone https://github.com/akulaakhilraj/CRICKET-CHATBOT

2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file:
   GROQ_API_KEY=your_key
   NEWS_API_KEY=your_key

4. Run the app:
   streamlit run app.py



Future Improvements

- Add RAG for player stats and history
- Improve score accuracy with official APIs
- Add voice assistant
- Deploy on cloud



Demo 


<img width="1777" height="971" alt="image" src="https://github.com/user-attachments/assets/a5af5eec-c31f-4498-a09e-8eb25b2ec5fa" />
