def number_to_roman_numeral(number):
    
    inputt = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    output = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    
    answer = ''
    
    count = 0
    
    while number > 0:
        for i in range(number // inputt[count]):
            answer += output[count]
            number -= inputt[count]
        count += 1
    print(answer)

number = int(input("Enter a number: "))
number_to_roman_numeral(number)
