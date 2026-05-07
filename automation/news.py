import requests

def get_news():
    newsapi = ""
    url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&apikey={newsapi}"

    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        return "No news available"

    headlines = [f"{i}. {article.get('title', '')}" for i, article in enumerate(articles, 1)]
    return "\n".join(headlines)

