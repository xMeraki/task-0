# Q5: Pandas and CSV Analysis
import pandas as pd
import os

df = pd.read_csv('data/student_performance.csv')

print("First 5 rows:\n", df.head())
print(f"\nNumber of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")
print("\nColumn names:", df.columns.tolist())
print("\nMissing values per column:\n", df.isnull().sum())

print(f"\nAverage Final_Score: {df['Final_Score'].mean():.2f}")

highest_student = df.loc[df['Final_Score'].idxmax()]
print(f"\nStudent with the highest Final_Score:\n{highest_student}")

# Create Improvement column using exact column names expected in output
df['Improvement'] = df['Final_Score'] - df['Previous Score']

print("\nStudents with attendance >= 80:\n", df[df['Attendance'] >= 80])

df_sorted = df.sort_values(by='Final_Score', ascending=False)

os.makedirs('data', exist_ok=True)
df_sorted.to_csv('data/processed_student_performance.csv', index=False)
print("\nProcessed DataFrame saved to 'data/processed_student_performance.csv'")