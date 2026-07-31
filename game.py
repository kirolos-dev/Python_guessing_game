import random

print("🎲 welcome to the guessing Game ¡")
secret_number = random.randint(1, 10)
attempt = 0

while True:
    guess = input("Enter a number between 1 and 10 :")
    guess = int(guess)
    attempt += 1
    
    if guess == secret_number:
        print(f"✅ correct you guessed the number in {attempt} attempts!")
        break
    elif guess > secret_number:
        print("⬆️ too high ¡ try again")
    else:
        print("⬇️ too low try again")
