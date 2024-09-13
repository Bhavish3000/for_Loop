""" This programe prints the following using for loop 
1. First 10 natural numbers
2. First 10 Whole numbers
3. First 10 even numbers
4. First 10 odd numbers
"""

number = int(input("Enter the number: "))

for index in range(0, number+1):
    if index >0:
        print(f"{index} is Natural number")

    print(f"{index} is whole number")

    if index%2 == 0:
        if index == 0 :
            continue
        print(f"{index} is Even number")
    else:
        print(f"{index} is odd number")
