import random 

random_number = random.randint(1,100)

while True:
    chosen_number = int(input("Please write your number between (1-100): "))
    
    if chosen_number == random_number :
        print("Well done. You found the right number.")
        break
    
    elif chosen_number < random_number:
        print("Increase your number.")
    
    else:
        print("Decrease your number.")