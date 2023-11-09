import random 


number = random.randint(0,99)

guessed = False 

attempts = 0 

print("Chose a number between 0 and 99.")

print("If you guess right, YOU WIN!")

while not guessed:
    
    user_number = int(input("Enter your guess: "))
    attempts += 1

    if user_number<number:
        print("It's a bigger number!")
    elif user_number>number:
        print("It's a smaller number!")
    else : 
        print("CONGRATULATIONS! YOU WIN!")
        guessed = True

print(f"You did it in {attempts} attemps.")
