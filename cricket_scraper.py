import requests
from bs4 import BeautifulSoup

def get_live_scores():
    url = "https://www.espncricinfo.com/live-cricket-score"

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        matches = soup.find_all("div", class_="ds-text-tight-m")[:3]

        results = []

        for match in matches:
            text = match.get_text(" ", strip=True)

            #provde with the text length
            if len(text) > 20:
                results.append(text)

        if not results:
            return "No clear live match data available."

        return "\n".join(results)

    except Exception as e:
        return f"Error fetching scores: {str(e)}"