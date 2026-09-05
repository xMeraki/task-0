# Q4: NumPy Basics
import numpy as np

hours_studied = np.array([2, 5, 3, 8, 4])
attendance = np.array([75, 90, 80, 95, 85])
previous_scores = np.array([60, 85, 70, 90, 75])
final_scores = np.array([70, 91, 58, 87, 76])

arrays = {
    "Hours Studied": hours_studied, 
    "Attendance": attendance, 
    "Previous Scores": previous_scores, 
    "Final Scores": final_scores
}

for name, arr in arrays.items():
    print(f"{name} - Shape: {arr.shape}, Dtype: {arr.dtype}")

print(f"\nMean Final Score: {np.mean(final_scores)}")
print(f"Max Final Score: {np.max(final_scores)}")
print(f"Min Final Score: {np.min(final_scores)}")
print(f"Standard Deviation of Final Scores: {np.std(final_scores):.2f}")

bonus_scores = final_scores + 5
print(f"Final Scores with 5 bonus marks: {bonus_scores}")

high_scorers_mask = final_scores >= 75
print(f"Boolean array (>= 75): {high_scorers_mask}")
print(f"Scores >= 75: {final_scores[high_scorers_mask]}")