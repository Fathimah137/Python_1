print("enter marks obtained in 5 subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0, 101)

if avg not in validRange:
    print("invalid input!:")

elif avg in range(91, 101):
    print("your grade is A1")
    
elif avg in range(81, 91):
    print("your grade is A2")

elif avg in range (71, 81):
    print("your grade is B1")

elif avg in range (61, 71):
    print("your grade is B2")

