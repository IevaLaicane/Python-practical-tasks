print("Calculate your gross salary for this week!")
user = input("Please enter your name: ")
hours = (float(input(user + ", please enter hours you worked this week: ")))

payrate = (float(input(user + ", please enter your payrate per hour: €")))

if hours > 40:
    overtime = hours - 40
    hours = hours - overtime
    newrate = payrate * 1.75
    salary = hours * payrate + overtime * newrate
else:
    salary = hours * payrate 

print(user + ", your gross salary for this week is €", salary)
