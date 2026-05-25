import random

rand_number = random.randint(1, 20)
versuche = 5
print("gesucht ist eine zahl zwischen 1 und 20, du hast 5 versuche findest du sie?")
while True:
    guess_raw = input("bitte gib eine tahl ein du hast:")
    if not guess_raw.isdigit():
        print(f"leider war das keine zahl.")
        continue

    guess = int(guess_raw)

    if guess == rand_number:
        print("Gewonnen!")
        break
    elif guess > rand_number:
        versuche -= 1
        print(f"leider zu hoch du hast noch {versuche} versuche.")
    elif guess < rand_number:
        versuche -= 1
        print(f"leider zu niedrieg du hast noch {versuche} versuche.")
    if versuche == 0:
        print("leider verloren")
        break
