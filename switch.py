try:
    temp = int(input("The Temp. is:"))
except:
    print("that was not an int. i will count with 25")
    temp = 25

try:
    target = int(input("What is the target:"))
except:
    print("that was not an int. i will count with 10")
    target = 10

####################################################
#Function that compares the temperature with the target
####################################################
def switch(temp, target):
    if temp < (target - 1):
        return "ON"
    elif temp >= (target + 1):
        return "OFF"
    else:
        return "SAME"

####################################################
#Function that outputs the result
####################################################
def state_output(temp, target):
    ergebnis = switch(temp, target)
    if ergebnis == "ON":
        print("Switch On")
    elif ergebnis == "OFF":
        print("Switch Off")
    else:
        print("nothing to do")




state_output(temp, target)

