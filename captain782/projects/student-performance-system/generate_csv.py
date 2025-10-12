import pandas as pd
import random

# Generate 100 student names
names = [f"Student_{i+1}" for i in range(100)]

# Define 10 columns
column = [
    "Name", "Math", "Science", "English", "History",
    "Attendance", "Participation", "Projects", "Discipline", "Creativity"
]

# Generate random scores for each student
data = []
for name in names:
    row = [name] + [random.randint(40, 100) for _ in range(9)]
    data.append(row)

# Create DataFrame and save to CSV

df = pd.DataFrame(data, columns=column)
df['Roll No'] = range(1, len(df) + 1)
df.set_index('Roll No',inplace=True)
df.to_csv("student_performance.csv", index='Name')

print(" CSV file with 100 students generated successfully.")


#print(df["Roll No"])
#print(df)