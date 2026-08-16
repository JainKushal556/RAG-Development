print("Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110].\nPrint all unique roll nums in the list.\n")

roll_numbers = [101, 105, 102, 101, 108, 105, 110]

print(set(roll_numbers))


# Given Employee records in the form of a list of tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)
# Example - [
# (101, "Alice", 50000),
# (102, "Bob", 65000),
# (103, "Charlie", 45000)
# ]

employees = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

user_id = int(input("Enter User Id :"))
for employee in employees:
    if(employee[0]==user_id):
        print("Employee Name: "+ str(employee[1]))
        print("Salary: "+ str(employee[2]))
        break
    else:
        print("..No Record Found..")