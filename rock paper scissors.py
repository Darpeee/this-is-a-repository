import random
print('Best Of Three Rounds Of Rock/Paper/Scissors')

def start():
    you=comp=stupid=0
    while you<2 and comp<2 and stupid<5:
        x=('Rock','Paper','Scissors')
        a = random.choice(x)
    
        b = input('Choose Between Rock/Paper/Scissors: ')
        b = b.capitalize()
    
        if a=="Rock":
            if b=="Rock":
                print("It's A Tie, Go Again")
            elif b=="Paper":
                print("You Won This Round")
                you+=1
            elif b=="Scissors":
                print("You Lost This Round")
                comp+=1
            else:
                print("Please Enter Valid Input")
                stupid+=1

        elif a=="Paper":
            if b=="Paper":
                print("It's A Tie, Go Again")
            elif b=="Scissors":
                print("You Won This Round")
                you+=1
            elif b=="Rock":
                print("You Lost This Round")
                comp+=1
            else:
                print("Plase Enter Valid Input")
                stupid+=1

        elif a=="Scissors":
            if b=="Scissors":
                print("It's A Tie, Go Again")
            elif b=="Rock":
                print("You Won This Round")
                you+=1
            elif b=="Paper":
                print("You Lost This Round")
                comp+=1
            else:
                print("Plase Enter Valid Input")
                stupid+=1

    if you==2:
        print("")
        print('You Won')
    
    elif comp==2:
        print("")
        print("You Lost")
    
    elif stupid==5:
        print("")
        z=('Randi Ho Tum','Chutiye Bhaag Ja','Sala','Apki Ma Ki Chut :3','NOOOOOOOOOOO')
        print(random.choice(z))
    
    else:
        print("Something Unpexted Happened")

    again = input('Wanna Go Again Y/N: ')
    start() if again.upper()=="Y" else print('Exiting') if again.upper()=="N" else print("Input Not Recognised, Exiting Anyway")

start()
    
    
