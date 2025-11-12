# Program: Will You Make It to Class on Time?

# Get user input
wake_up_time = int(input("What time did you wake up? (24-hour format, e.g., 7 for 7am, 13 for 1pm): "))
class_time = int(input("What time does your class start? (24-hour format): "))
get_ready_time = int(input("How many hours does it take you to get ready and travel to class? "))

# Calculate when you'll arrive
arrival_time = wake_up_time + get_ready_time

# Decision making using if, elif, else
if arrival_time < class_time:
    print("Nice! You’ll make it to class early. Maybe grab a coffee ☕.")
elif arrival_time == class_time:
    print("You made it just in time! Hurry before attendance starts! 🏃‍♂️")
else:
    print("Oh no! You’re going to be late for class! 😬")

# Optional: add a fun motivation
if arrival_time > class_time + 1:
    print("Might as well grab breakfast and plan to be early for the next one 😅.")
else:
    print("Good effort! Keep that schedule tight ⏰.")
