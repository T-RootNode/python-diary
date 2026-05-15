####################################################
# Thing 02 - 15.05.2026
#
# WHAT I LEARNED:
#   - while CONDITION: runs as long as condition is True
#   - loops stops automatically when condition becomes False
#   - code without indentation runs after the loop once
#   - while True: runs forever, needs breake to stops
#
####################################################

temperatur = 15

while temperatur < 25:
    print(f"zu kalt:{temperatur} °C")
    temperatur = temperatur + 1

print(f"Erreicht: {temperatur} °C")

