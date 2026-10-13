import pandas as pd

#Load both files
students_df = pd.read_csv('students.csv')
scores_df = pd.read_csv('scores.csv')

#Check missing values
print("Missing values in students.csv:\n", students_df.isnull().sum())
print("Missing values in scores.csv:\n", scores_df.isnull().sum())

#Fill or remove missing data appropriately
students_df = students_df.dropna(subset=['student_id'])
scores_df = scores_df.dropna(subset=['student_id'])

#Interpolate numeric columns
for df in [students_df, scores_df]:
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].interpolate(method='linear')
    df[numeric_cols] = df[numeric_cols].bfill().ffill()

#Fill missing values
students_df['major'] = students_df['major'].fillna('Undeclared')
students_df['name'] = students_df['name'].fillna('Unknown')

#Merge the two datasets
merged_df = pd.merge(students_df, scores_df, on='student_id')
print("\n--- 4. Merged Dataset (First 5 Rows) ---")
print(merged_df.head())

#Calculate each student's average score across subjects
score_columns = ['python', 'math', 'database']
merged_df['average_score'] = merged_df[score_columns].mean(axis=1)

student_averages = merged_df[['student_id', 'name', 'major', 'average_score']]
print("Student Average Scores")
print(student_averages.head())

# 6. Find the top 5 students based on average score
top_5_students = student_averages.sort_values(by='average_score', ascending=False).head(5)
print("Top 5 Students")
print(top_5_students)

#Compute average score by major
avg_score_by_major = merged_df.groupby('major')['average_score'].mean().reset_index()
avg_score_by_major.rename(columns={'average_score': 'overall_major_average'}, inplace=True)
print("Average Score by Major")
print(avg_score_by_major)