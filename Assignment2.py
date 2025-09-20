# Program Name: Assignment2.py
# Course: IT3883/Section 01
# Student Name: Jordon James
# Assignment Number: 2
# Due Date: 9/19/2025
# Purpose: This program reads student names and their six scores from an input file,
#          calculates each student's average score, and prints the results
#          in descending order by grade.
# -------------------------------------------------------------



# opens the file and reads the lines
with open("Assignment2input.txt", "r") as file:  
    lines = file.readlines()

# make a empty list to store student names and averages
students = []

# process each line in the file
for line in lines:
    parts = line.strip().split()  # splits line into fields
    name = parts[0]               # first part is the student's name
    scores = list(map(float, parts[1:]))  # convert numbers to floats
    average = sum(scores) / len(scores)   # calculates the average
    students.append((name, average))      # store as (name, average) tuple

# sort students in descending order by average
students.sort(key=lambda x: x[1], reverse=True)

# print results
for student in students:
    print(f"{student[0]} {student[1]:.2f}")  # Format to 2 decimal places
