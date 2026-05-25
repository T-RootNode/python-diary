import random

rand_number = random.randint(1, 20)
versuche = 5

print("Gesucht ist eine Zahl zwischen 1 und 20. Du hast 5 Versuche. Findest du sie?")

while True:
    guess_raw = input("Bitte gib eine Zahl ein: ")

    if not guess_raw.isdigit():
        print("Leider war das keine Zahl.")
        continue

    guess = int(guess_raw)

    if guess == rand_number:
        print("Gewonnen!")
        print("Drücke ENTER zum Beenden...")
        input()
        break
    elif guess > rand_number:
        versuche -= 1
        print(f"Leider zu hoch! Du hast noch {versuche} Versuche.")
    elif guess < rand_number:
        versuche -= 1
        print(f"Leider zu niedrig! Du hast noch {versuche} Versuche.")

    if versuche == 0:
        print("Leider verloren!")
        print(f"Die Zahl war {rand_number}")
        print("Drücke ENTER zum Beenden...")
        input()
        break
