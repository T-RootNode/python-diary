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

----------------------------------------------------------------------
CRITICAL ADHS-RULES (Avoid Overwhelm):
1. Build the features ONE BY ONE.
2. Start with Option 4 (Exit) so you can close the game.
3. Then build Option 2 (Add) and Option 1 (View) to see if it works.
4. Build Option 3 (Drop) last. Remember to check if the backpack
   is empty BEFORE using .pop(), otherwise the game crashes!

Go for it! Write your code right below this block.
======================================================================
"""

def show_menue():
    print("=========Welcome to the Backpack Game=========")
    print()
    print("Please use numbers as input")
    print()
    print("1) view")
    print("2) add")
    print("3) drop")
    print("4) quit")

backpack = []

while True:
    show_menue()
    input_raw = input("input here please:")

    if not input_raw.isdigit():
        print("Sadly that was not a number.")
        continue
    input_int = int(input_raw)

    if input_int == 4:
        print("bye see you soon.")
        break
    if input_int == 2:
        new_item = input("What you like to add to your Backpack:")
        backpack.append(new_item)
    if input_int == 1:
        print(f"In your Backpack is: {backpack}")
    if input_int == 3:
        if len(backpack) == 0:
            print("there is nothing to drop.")
        else:
            print("Drop the last item in the Backpack")
            backpack.pop()
