import pandas as pd

df = pd.read_csv('students.csv')

print("First five rows")
print(df.head(5)) #without input, it is 5 rows by default

rows, columns = df.shape #dataframe
print(f"\nNumber of rows: {rows}, Number of columns: {columns}")

print("Name and GPA")
name_and_gpa = df[['name', 'GPA']]
print(name_and_gpa.head())

print("Sorted GPA")
sorted_gpa = df.sort_values(by='GPA' , ascending=False)
print(sorted_gpa)

print("Students with GPA >= 3.5")
high_gpa = df[df['GPA'] >= 3.5]
print(high_gpa)

print("Average GPA by Majors")
avg_by_major = df.groupby('major')['GPA'].mean()
print(avg_by_major)

