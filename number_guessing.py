import random
#number guessing game
print("welcome to the number guessing game!")
print("guess a number between 1 and 100")
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5
for attempts in range(1, max_attempts +1):
    print(f"/n attempt {attempts} of {max_attempts}")


# while True:
    guess = int(input("Enter your guess: "))
    attempts +=1

    if guess > secret_number:
        print(" Number is high, try again")
    elif guess< secret_number:
        print("Number is low, try again")

    else:
        print(f" Correct! you guessed it in {attempts} attempts")
        # break


print(f"attempts left: {max_attempts - attempts}")
if guess != secret_number:
    print(" Game over!, you've used all your 5 attempts")
    print(" The correct answer was:", secret_number)




    