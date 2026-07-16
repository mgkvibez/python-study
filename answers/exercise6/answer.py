age = 18 

if age >= 21:
    print("You can enter the club and can buy drinks.")
elif age >= 18:
    print("You can enter the club but cannot buy drinks.")
else:
    print("You are too young to enter the club")

    has_id  = True
    is_vip = False

name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")

x = 10 
status = "even" if x % 2 == 0 else "odd"
print(status)

command = "start"

match command:
    case "start":
        print("Starting the system...")
    case "stop" | "halt":
        print("Stopping the system...")
    case _:
        print("Unknown command.")


mark = 92
if mark >= 90 and mark <= 100:
    print("A")
elif mark < 90 and mark >= 80:
    print("B")
elif mark < 80 and mark >= 70:
    print("C")
else: 
    print ("F")

score = 85
if score >= 90 and score <= 100 :
    print(f"score is {score}, EXCELLENT!" )
elif score < 90 and score >= 70 :
    print(f"score is {score}, GOOD!")
elif score < 70 and score >= 0:
    print(f"score is {score}, NEEDS IMPROVEMENT!")
else:
    print("invalid score, score must be between 0 to 100")
