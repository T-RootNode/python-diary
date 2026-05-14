####################################################
# Thing 01 - 14.05.2026
#
# WHAT I LEARNED:
#
# Functions - def my_function(parameter):
#   A function is a reusable block of code.
#   Parameters are placeholders filled when called.
#   Static:  temp = 22        (always 22)
#   Dynamic: def f(temp):     (filled at call time)
#
# if / elif / else
#   The basic decision logic.
#   One condition is always true, rest is skipped.
#
# Hysteresis
#   Without a dead band, a switch would flutter
#   on and off rapidly at the threshold.
#   Solution: separate ON and OFF thresholds.
#   ON  below target - 1
#   OFF above target + 1
#   SAME in between -> do nothing
#   This protects hardware from rapid switching.
#
# return vs print
#   return sends a value back to the caller.
#   print just outputs to the screen.
#   A function that returns can be used by other
#   functions. A function that only prints cannot.
#
# try / except
#   try:  attempt something that could fail
#   except: catch the error, handle it gracefully
#   Instead of crashing, the program continues
#   with a fallback value.
#
# Calling functions
#   Defining a function does nothing by itself.
#   It is just a blueprint.
#   You have to call it to make it run.
#   state_output(temp, target)  <-- this runs it
#
####################################################

try:
    temp = int(input("The Temp. is: "))
except:
    print("That was not an int. Counting with 25.")
    temp = 25

try:
    target = int(input("What is the target: "))
except:
    print("That was not an int. Counting with 10.")
    target = 10

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

state_output(temp, target)
