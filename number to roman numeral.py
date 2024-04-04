print('converts number to roman numerals only accepts till 3999')
def number_to_roman_numeral():
    a=int(input('enter a number to be converted: '))
    b=str(a)
    unit=''
    ten=''
    hundred=''
    thousand=''
    flag=0

    for i in b:
    
        c=a%10

        if a>3999:
            print('bye')
            break
    
        elif flag==0:
            if c<4 and c!=0:
                unit+=c*'I'
            elif c==4:
                unit+='IV'
            elif c==5:
                unit+='V'
            elif c>5 and c<9:
                unit+='V'
                unit+=(c-5)*'I'
            elif c==9:
                unit+='IX'
        
        elif flag==1:
            if c<4 and c!=0:
                ten+=c*'X'
            elif c==4:
                ten+='XL'
            elif c>5 and c<9:
                ten+='L'
                ten+=(c-5)*'X'
            elif c==9:
                ten+='XC'

        elif flag==2:
            if c<4 and c!=0:
                hundred+=c*'C'
            elif c==4:
                hundred+='CD'
            elif c>5 and c<9:
                hundred+='D'
                hundred+=(c-5)*'C'
            elif c==9:
                hundred+='CM'

        elif flag==3:
            if c<4 and c!=0:
                thousand+=c*'M'
            
        a=a//10
        flag+=1

    answer=thousand+hundred+ten+unit
    print(answer)

number_to_roman_numeral()
