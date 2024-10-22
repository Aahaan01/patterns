number=int(input("Please enter a number: "))
for i in range(number):
    for j in range(i+1):
        print("*",end="&")
    print()