"""
MISSION: PROJECT FROSTBITE - THE SMART HOME CLIMATE MATRIX

STORY:
You are running the climate control matrix for a sensitive greenhouse sector.
If the temperature gets too high, the crops spoil. If it gets too cold, they freeze.
Your job is to build an interactive simulation loop.

--------------------------------------------------------------------------------

TECHNICAL REQUIREMENTS:

1. The State Dictionary:
   Initialize a dictionary named 'greenhouse' with three keys:
   * "current_temp" (start value: 28)
   * "target_temp" (start value: 22)
   * "ac_status" (start value: False)

2. The Main Loop (while True):
   The simulator must run continuously, showing the dashboard and asking
   for user input on every iteration.

3. The Dashboard Display:
   At the start of every loop iteration, print the current status beautifully.
   Example: [AC: OFF] | Current: 28°C | Target: 22°C

4. The Automation Logic:
   * If "current_temp" > "target_temp" -> "ac_status" becomes True.
   * If "ac_status" is True -> "current_temp" drops by 1 degree on that turn.
   * If "current_temp" <= "target_temp" -> "ac_status" becomes False.

5. User Actions (input()):
   Provide 3 simple choices:
   * '1' : Wait (does nothing, lets the simulation tick forward one step)
   * '2' : Change Target Temperature (prompts for a number, validates with .isdigit())
   * '3' : Exit the simulation (break)

--------------------------------------------------------------------------------

GAMIFIED CHECKLIST (Delete the ' ' and put an 'X' when achieved!):

[ ] Milestone 1: Dictionary initialized and dashboard prints correctly.
[ ] Milestone 2: Main loop running (Option 1 and Option 3 work smoothly).
[ ] Milestone 3: Option 2 (Change Target) secured with .isdigit() validation.
[ ] Milestone 4: BOSS FIGHT: Automation logic connected. Pressing '1' repeatedly
                   makes the temperature drop automatically until it hits the
                   target, and then the AC instantly shuts off.

RULE: No finished code from the AI – you build this matrix yourself!
"""


greenhouse = {
    "current_temp": 28,
    "target_temp": 22,
    "ac_status": False
}
ac = "OFF"

while True:
    print(f"Current Temperature is: {greenhouse['current_temp']}")
    print(f"Target is: {greenhouse['target_temp']}")
    print(f"AC is currently: {ac}")

    if greenhouse['target_temp'] < greenhouse['current_temp']:
        greenhouse['ac_status'] = True
    elif greenhouse['target_temp'] == greenhouse['current_temp']:
        greenhouse['ac_status'] = False

    if greenhouse['ac_status'] is True:
        ac = "ON"
    elif greenhouse['ac_status'] is False:
        ac = "OFF"

    if greenhouse['target_temp'] < greenhouse['current_temp']:
        greenhouse['current_temp'] = greenhouse['current_temp'] - 1
    elif greenhouse['current_temp'] == greenhouse['target_temp']:
        print("Temperature is OK!")
        input("Press Enter to Exit...")
        break

