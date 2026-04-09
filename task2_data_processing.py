import json
import csv

with open("data/trends_20260407.json", "r") as f:
    data = json.load(f)

print("Total records:", len(data))

with open("data/cleaned_trends.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["post_id", "title", "category", "score", "num_comments", "author", "collected_at"])

    for item in data:
        writer.writerow([
            item.get("post_id"),
            item.get("title"),
            item.get("category"),
            item.get("score"),
            item.get("num_comments"),
            item.get("author"),
            item.get("collected_at")
        ])

print("CSV file created successfully")