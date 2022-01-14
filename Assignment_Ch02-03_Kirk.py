firstName = input("Enter your first name: ")
payPerHour = float(input("Enter your pay rate per hour: "))
hoursWorked = float(input("Enter the number of hours you worked last week: "))

print("\n")
print("First Name: ", firstName)
print("Pay Rate: ${:5.2f}".format(payPerHour))
print("Hours Worked: ", hoursWorked)
print("Salary: ${:5.2f}".format(payPerHour * hoursWorked))
