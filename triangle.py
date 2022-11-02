n=int(input('how many rows do you want: '))
h=1
for j in range(n,0,-1):
    print(" "*j, "*"*h)
    h+=2
