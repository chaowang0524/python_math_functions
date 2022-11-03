"""Find the max, min and mean score of the students in each course"""

# create a dictionary: key = coures, values = list of grades
course_grade = {}

with open("Course_grade_input.txt") as f:
    for line in f:
        line = line[:-1]  # remove \n at the end
        course, sno, name, grades = line.split(",")  # split into 4 values
        if course not in course_grade:
            course_grade[course] = []
        course_grade[course].append(int(grades))


for course, grades in course_grade.items():
    print(course,
          max(grades),
          min(grades),
          sum(grades)/len(grades))
