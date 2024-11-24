import random

top_range = input("Enter the highest range of number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Enter a number greater than Zero Next Time!")
        quit()
else:
    print("Please enter a number Next Time!")
    quit()

random_number = random.randint(0,top_range)

guess=0
while True:
    guess+=1
    user_guess = input("Guess The Number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please Guess a number Next Time!")
        continue
    
    if user_guess == random_number:
        print("You are right")
        print("You Got it in",guess,"attempts")
        break
    else:
        if guess > top_range:
            print("You are above the limit")
        else:
            print("You are below the limit")

print("You Got it in",guess,"attempts")
