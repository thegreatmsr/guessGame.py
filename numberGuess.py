import random
top_of_range = input("Type a number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number:")
    quit()
random_number = random.randint(0,top_of_range)


while True:
    user_Guess=input("Make a guess:")
    if user_Guess.isdigit():
     user_Guess=int(user_Guess)
    
    else:
       print("Please type a number:")
       continue
    if user_Guess==random_number:
        print("You got it!")
        break
    else:
        print("You got it incorrect")
    
    
    
    
    
    


