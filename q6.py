# Q6: Visualizing the Data with Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('plots', exist_ok=True)
df = pd.read_csv('data/processed_student_performance.csv')

# 1. Bar chart: Student names vs final scores
plt.figure(figsize=(10, 6))
plt.bar(df['Student'], df['Final_Score'], color='skyblue')
plt.title('Student Final Scores')
plt.xlabel('Student Name')
plt.ylabel('Final Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plots/final_scores.png')
plt.close()

# 2. Scatter plot: Hours studied vs final score
plt.figure(figsize=(8, 5))
plt.scatter(df['Hours Studied'], df['Final_Score'], color='green')
plt.title('Impact of Study Hours on Final Score')
plt.xlabel('Hours Studied')
plt.ylabel('Final Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/study_vs_score.png')
plt.close()

# 3. Histogram: Distribution of final scores
plt.figure(figsize=(8, 5))
plt.hist(df['Final_Score'], bins=10, color='purple', edgecolor='black')
plt.title('Distribution of Final Scores')
plt.xlabel('Final Score Range')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('plots/score_distribution.png')
plt.close()

# 4. Custom plot: Attendance vs Final Score
plt.figure(figsize=(8, 5))
plt.scatter(df['Attendance'], df['Final_Score'], color='orange', marker='^')
plt.title('Attendance vs Final Score')
plt.xlabel('Attendance (%)')
plt.ylabel('Final Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/custom_plot.png')
plt.close()