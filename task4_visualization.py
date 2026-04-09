import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_trends.csv")

counts = df["category"].value_counts()

plt.figure()
counts.plot(kind="bar")
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

avg = df.groupby("category")["score"].mean()

plt.figure()
avg.plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.show()