"""Counting the number of student who like certain sport"""

# create a dictionary to store sport as key and number as value

habit_count = {}
habit_list = []
with open("habits.txt") as f:
    for line in f:
        line = line[:-1]
        sname, habit_1, habit_2 = line.split(",")
        habit_list = [habit_1, habit_2]
        # Count the habit in the dictionary
        for habit in habit_list:  # iterate the everyone's habit and put it into the dictionary
            if habit not in habit_count:  # create the key if it doesn't exist
                habit_count[habit] = 0
            habit_count[habit] += 1

print(habit_count)
