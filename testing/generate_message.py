names = input("Enter names separated by commas: ").split(",")
assignments = input("Enter assignments separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"

for i in range(4):
    current_grade = grades[i]
    missing_assignments = assignments[i]
    possible_grade = int(current_grade) + 2 * int(missing_assignments)
    print(message.format(names[i], missing_assignments, grades[i], possible_grade))

