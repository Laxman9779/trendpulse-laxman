import pandas as pd
 
df = pd.read_csv("data/cleaned_trends.csv")

print("Total records:", len(df))

print("\nStories per category:")
print(df["category"].value_counts())

top_story = df.loc[df["score"].idxmax()]

print("\nTop Story:")
print(top_story["title"])
print("Score:", top_story["score"])

print("\nAverage score per category:")
print(df.groupby("category")["score"].mean())

print("\nTotal comments per category:")
print(df.groupby("category")["num_comments"].sum())