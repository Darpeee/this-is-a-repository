print('Best Of Three Rounds Of Rock/Paper/Scissors')

def Stone_Paper_Scissors():
    choice=['Stone','Paper','Scissors']
    gali=['Sala','Randi','Madrchod','Bhen Ka Lund','Teri Maki','Chutiye','Sahi Se Khel','Bhaag Ja Madrchod']
    import random
    
    x=y=z=0
    while x<3 and y<3:
        
        computer=random.choice(choice)
        player=(input('Stone, Paper, Scissors?: '))
        
        if player.capitalize()=='Stone' or player.capitalize()=='Paper' or player.capitalize()=='Scissors':
            z=0
        if z==5:
            print(random.choice(gali))
            continue
        
        if computer=='Stone':
            if player.capitalize()=='Stone':
                print('Draw')
            if player.capitalize()=='Paper':
                print('Win')
                x+=1
            if player.capitalize()=='Scissors':
                print('Lose')
                y+=1
            else:
                z+=1
                
        elif computer=='Paper':
            if player.capitalize()=='Stone':
                print('Lose')
                y+=1
            if player.capitalize()=='Paper':
                print('Draw')
            if player.capitalize()=='Scissors':
                print('Win')
                x+=1
            else:
                z+=1
                
        elif computer=='Scissors':
            if player.capitalize()=='Stone':
                print('Win')
                x+=1
            if player.capitalize()=='Paper':
                print('Lose')
                y+=1
            if player.capitalize()=='Scissors':
                print('Draw')
            else:
                z+=1

    if x>=3:
        print('You Win')
    elif y>=3:
        print('You Lose')
    else:
        print('Something Unexpected Happened')
        
    umm=input('Play Again? Y/N: ')   
    Stone_Paper_Scissors() if umm.upper()=='Y' else print('Exiting....')
    
Stone_Paper_Scissors()
