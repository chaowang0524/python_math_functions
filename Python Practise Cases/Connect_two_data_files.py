# Create a dictionary to store the info file:
course_info = {}

with open("Course_info.txt") as f:
    for line in f:
        line = line[:-1]
        course, lecturer = line.split(",")
        if course not in course_info:
            course_info[course] = lecturer  # set keys and values
    print(course_info)

# Append the lecturers' name to the end of the grade file:
output_list = []
with open("Course_grade_input.txt") as file:
    for line in file:
        line = line[:-1]
        print(line)
        cname, sno, sname, sgrade = line.split(",")
        # `cname` literally is the same as 'course' in the dictionary `course_info`
        # so use .get() method to get the value from the dictionary
        lecturer = course_info.get(cname)
        output = cname, lecturer, sno, sname, sgrade
        # output_list.append(output)
        # print to new file
        with open("Course_grade_output.txt", "a") as output_file:
            print(output, file=output_file, sep="\n")
