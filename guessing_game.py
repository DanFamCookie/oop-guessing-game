# answer is a number in the guessing game 
# our guessing game function has been created 
# guess is a method that takes a number called user_guess
#guess should print

# user_input = input("What is your name: ")
# print(f'Welcome {user_input} Lets play')
# user_guess = int(input("pick your number: "))
# print(user_guess)


# class GuessingGame:
#     def __init__(self, answer, solved):
#         self.answer = answer


#     def solved(self):
#         return "great you solved it"
    
# game = GuessingGame(10)

# last_guess = 0
# last_result = 0

# while game.solved() == False:
# if last_guess != None:
#     print(f"Ooops! Your last guess ({last_guess}) was {last_result}.")
#     print("")



# import random

# # Define your GuessingGame class here...


# # ----- DRIVER CODE -----
# game = GuessingGame(random.randint(1,100))
# last_guess  = None
# last_result = None

# while game.solved() == False:
#   if last_guess != None: 
#     print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
#     print("")

#   last_guess  = input("Enter your guess: ")
#   last_result = game.guess(last_guess)


# print(f"{last_guess} was correct!")

import random
print ('Welcome to the guessing game!\n')
class GuessingGame():
    def __init__(self, answer):
        self.answer = answer      
        self.user_guess = None
        
    def guess(self, user_guess):
        self.user_guess = user_guess 
        if user_guess == self.answer:
            return 'Correct'
        elif user_guess > self.answer:
            return 'High'
        else:
            return 'Low'
    def solved(self):
        return self.user_guess == self.answer 
    
game = GuessingGame(random.randint(1,100))

last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)

print(f"{last_guess} was correct!")