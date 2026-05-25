"""
======================================================================
CHALLENGE: THE MAGIC BACKPACK (Text-Adventure Inventory)
======================================================================

STORY:
You are coding the inventory logic for a classic RPG text adventure.
Your hero is exploring a dungeon and finding loot!

YOUR TASK:
Write an interactive console program where the player manages their
backpack. The game runs in an endless loop (while True) and offers
the player a menu with 4 actions:

1. View: Show all items currently in the backpack.
2. Add: The player types in a new item name to add it.
3. Drop: The player removes the LAST item they picked up.
4. Exit: Ends the game.

----------------------------------------------------------------------
YOUR TOOLS: LISTS (lists)

* Create an empty list:
  backpack = []

* Add something to the end of the list:
  backpack.append("Shield")

* Remove the last item from the list:
  backpack.pop()
  (This automatically deletes whatever is at the very end).

* Check how many items are in the list:
  len(backpack)
  (If it is 0, the backpack is empty!)

======================================================================
"""

def show_menu():
    print("========= Welcome to the Backpack Game =========")
    print()
    print("Please use numbers as input")
    print()
    print("1) View")
    print("2) Add")
    print("3) Drop")
    print("4) Quit")

backpack = []

while True:
    show_menu()
    input_raw = input("Input here please: ")

    if not input_raw.isdigit():
        print("Sadly, that was not a number.")
        continue
    input_int = int(input_raw)

    if input_int == 4:
        print("Goodbye, see you soon!")
        break

    if input_int == 2:
        new_item = input("What would you like to add to your backpack?: ")
        backpack.append(new_item)
        print(f"'{new_item}' has been added to your backpack.")

    if input_int == 1:
        if len(backpack) == 0:
            print("Your backpack is currently empty.")
        else:
            print(f"In your backpack is: {backpack}")

    if input_int == 3:
        if len(backpack) == 0:
            print("There is nothing to drop.")
        else:
            # Clever move: we check the last item BEFORE popping it
            removed_item = backpack[-1]
            backpack.pop()
            print(f"Dropped the last item from the backpack: '{removed_item}'")
