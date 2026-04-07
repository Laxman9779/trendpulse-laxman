import requests
import json
import os
from datetime import datetime

technology_keywords = ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"]
worldnews_keywords = ["war", "government", "country", "president", "election", "climate", "attack", "global"]
sports_keywords = ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"]
science_keywords = ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"]
entertainment_keywords = ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent":"TrendPulse/1.0"}

res = requests.get(url, headers=headers)
story_ids = res.json()

all_data = []

counts = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

for story_id in story_ids:

    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_res = requests.get(story_url, headers=headers)

    if story_res.status_code != 200:
        continue

    story = story_res.json()
    title = story.get("title", "").lower()

    category = None

    if any(word in title for word in technology_keywords):
        category = "technology"
    elif any(word in title for word in worldnews_keywords):
        category = "worldnews"
    elif any(word in title for word in sports_keywords):
        category = "sports"
    elif any(word in title for word in science_keywords):
        category = "science"
    elif any(word in title for word in entertainment_keywords):
        category = "entertainment"

    if category is None:
        continue

    if counts[category] >= 25:
        continue

    data = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score"),
        "num_comments": story.get("descendants"),
        "author": story.get("by"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    all_data.append(data)
    counts[category] += 1

    if sum(counts.values()) >= 125:
        break

if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(all_data, f, indent=4)

print(f"Collected {len(all_data)} stories. Saved to {filename}")