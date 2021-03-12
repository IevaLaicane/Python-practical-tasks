print("Calculate your gross salary for this week!")
user = input("Please enter your name: ")
hours = (float(input(user + ", please enter hours you worked this week: ")))

payrate = (float(input(user + ", please enter your payrate per hour: €")))
salary = hours * payrate 
print(user + ", your gross salary for this week is €", salary)
