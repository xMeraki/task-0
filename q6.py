import os
import matplotlib.pyplot as plt
import pandas as pd

# Ensure the plots directory exists
os.makedirs("plots", exist_ok=True)

# Load the processed dataset from Q5
df = pd.read_csv("data/processed_student_performance.csv")

# ---------------------------------------------------------
# 1. Bar Chart: Student names vs final scores
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))
plt.bar(df["Student"], df["Final_Score"], color="skyblue", edgecolor="black")
plt.title("Student Names vs Final Scores")
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 105)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("plots/final_scores.png")
plt.close()

# ---------------------------------------------------------
# 2. Scatter Plot: Hours studied vs final score
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Hours_Studied"],
    df["Final_Score"],
    color="darkorange",
    edgecolor="black",
    s=70,
    alpha=0.85,
)
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/study_vs_score.png")
plt.close()

# ---------------------------------------------------------
# 3. Histogram: Distribution of final scores
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(
    df["Final_Score"],
    bins=8,
    color="mediumseagreen",
    edgecolor="black",
    alpha=0.8,
)
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score Range")
plt.ylabel("Number of Students")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/score_distribution.png")
plt.close()

# ---------------------------------------------------------
# 4. Custom Plot: Attendance vs Improvement
# (Shows how attendance relates to score gain/loss from previous test)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Attendance"],
    df["Improvement"],
    c=df["Final_Score"],
    cmap="viridis",
    s=80,
    edgecolor="black",
    alpha=0.85,
)
cbar = plt.colorbar()
cbar.set_label("Final Score")
plt.axhline(0, color="red", linestyle="--", linewidth=1, label="No Change (0)")
plt.title("Attendance vs Score Improvement")
plt.xlabel("Attendance (%)")
plt.ylabel("Improvement (Final - Previous)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/custom_plot.png")
plt.close()

print("All plots generated and saved in plots/")