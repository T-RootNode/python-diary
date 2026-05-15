####################################################
# Thing 03 - 15.05.2026
#
# WHAT I LEARNED:
#   - while True: runs forever, needs break to stop
#   - indentation decides what belongs to the loop
#   - input() always returns a string - save it before
#     converting, so you can check it in except
#   - except can check what the user typed (q = quit)
#
####################################################

# Compares temperature against target with hysteresis
def switch(temp, target):
    if temp < (target - 1):
        return "ON"
    elif temp >= (target + 1):
        return "OFF"
    else:
        return "SAME"

# Outputs the result in human readable form
def state_output(temp, target):
    result = switch(temp, target)
    if result == "ON":
        print("Switch On")
    elif result == "OFF":
        print("Switch Off")
    else:
        print("Nothing to do")

while True:
    try:
        user_input = input("the temp is: (q for quit)")
        temp = int(user_input)
    except:
        if user_input == "q":
            break
        print("That was not an int. Counting with 25.")
        temp = 25

    try:
        user_input = input("What is the target: (q for quit)")
        target = int(user_input)
    except:
        if user_input == "q":
            break
        print("That was not an int. Counting with 10.")
        target = 10


    state_output(temp, target)

