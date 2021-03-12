print("Calculate your gross salary for this week!")
user = input("Please enter your name: ")

while True:
    try:
        hours = (float(input(user + ", please enter hours you worked this week: ")))
        break
    except ValueError:
        print ("That's not a number. Try again!")

while True:        
    try:
        payrate = (float(input(user + ", please enter your payrate per hour: €")))
        break
    except ValueError:
        print ("That's not a number. Try again!")
        
if hours > 40:
    overtime = hours - 40
    hours = hours - overtime
    newrate = payrate * 1.75
    salary = hours * payrate + overtime * newrate
else:
    salary = hours * payrate 

print(user + ", your gross salary for this week is €", salary)
