import matplotlib.pyplot as plt
import pandas as pd

# 1. Load scores.csv into a DataFrame
df = pd.read_csv("scores.csv")

plt.figure(figsize=(8, 6))
plt.scatter(
    df.index, df["math"], color="blue", label="Math", alpha=0.7, edgecolors="k"
)
plt.scatter(
    df.index,
    df["python"],
    color="green",
    label="Python",
    alpha=0.7,
    edgecolors="k",
)
plt.scatter(
    df.index,
    df["database"],
    color="orange",
    label="DB",
    alpha=0.7,
    edgecolors="k",
)

plt.title("Student Scores Scatter Plot")
plt.xlabel("Student Index")
plt.ylabel("Scores")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("scattered.png", dpi=300)
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

axes[0].hist(df["math"], bins=10, color="skyblue", edgecolor="black")
axes[0].set_title("Math Marks")
axes[0].set_xlabel("Score Range")
axes[0].set_ylabel("Frequency")
axes[0].grid(axis="y", linestyle="--", alpha=0.7)

axes[1].hist(df["python"], bins=10, color="lightgreen", edgecolor="black")
axes[1].set_title("Python Marks")
axes[1].set_xlabel("Score Range")
axes[1].grid(axis="y", linestyle="--", alpha=0.7)

axes[2].hist(df["database"], bins=10, color="sandybrown", edgecolor="black")
axes[2].set_title("DB Marks")
axes[2].set_xlabel("Score Range")
axes[2].grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig("histo.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 6))
df[["math", "python", "database"]].boxplot()
plt.title("Box Plot of Course Marks")
plt.ylabel("Scores")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("box.png", dpi=300)
plt.close()