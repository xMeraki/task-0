import pandas as pd

# 1. Load the CSV into a DataFrame
# Relative path assumes you run the script from inside task-0/
df = pd.read_csv("data/student_performance.csv")

# 2. Print the first five rows
print("--- First 5 Rows ---")
print(df.head())
print()

# 3. Print the number of rows and columns
rows, cols = df.shape
print(f"Dataset Dimensions: {rows} rows, {cols} columns\n")

# 4. Display the column names
print("Column Names:")
print(list(df.columns))
print()

# 5. Check whether the dataset contains missing values
print("Missing Values per Column:")
print(df.isnull().sum())
print()

# 6. Calculate the average Final_Score
avg_final_score = df["Final_Score"].mean()
print(f"Average Final Score: {avg_final_score:.2f}\n")

# 7. Find the student with the highest Final_Score
top_student = df.loc[df["Final_Score"].idxmax()]["Student"]
max_score = df["Final_Score"].max()
print(f"Highest Final Score: {top_student} ({max_score})\n")

# 8. Create a new column: Improvement = Final_Score - Previous_Score
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

# 9. Display only students with attendance greater than or equal to 80
high_attendance = df[df["Attendance"] >= 80]
print("Students with Attendance >= 80%:")
print(high_attendance)
print()

# 10. Sort the DataFrame by Final_Score in descending order
df_sorted = df.sort_values(by="Final_Score", ascending=False)
print("DataFrame Sorted by Final_Score (Descending):")
print(df_sorted)
print()

# 11. Save the processed DataFrame as processed_student_performance.csv
# index=False avoids saving the row indices as an extra column
df_sorted.to_csv("data/processed_student_performance.csv", index=False)
print("Successfully saved to data/processed_student_performance.csv")