import time
import random
i=1
print('guess the number :3')
print('so the number will be between 1 to 10 for starters')
number = random.randint(1,10)
#generates a random number from 1 to 10
time.sleep(2)
guess=int(input('time for you to start guessing: '))
while guess>number and i<3:
    i+=1 #adding counter for no. of guesses
    if guess>10:
        print('please guess between the range 1 to 10')
        break
    elif guess-number>2:
        print ('too high')
        time.sleep(1)
        guess=int(input('try again: '))
    elif guess-number<=2:
        print('you are close')
        time.sleep(1)
        guess=int(input('try again: '))
while guess<number and i<3:
    i+=1 #adding counter for no. of guesses
    if guess<0:
        print('please guess between the range 1 to 10')
        break
    elif number-guess>2:
        print ('too low')
        time.sleep(1)
        guess=int(input('try again: '))
    elif number-guess<=2:
        print ('you are close')
        time.sleep(1)
        guess=int(input('try again: '))
if number==guess:
    print('congratulations, you have guessed the number correctly')
elif guess<0 or guess>10:
    print('you are weird, please restart the program')
elif number!=guess:
    print('the number was',number,'. nice try, better luck next time')
    
    
