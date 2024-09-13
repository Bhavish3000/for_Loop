"""This program prints first 10 integers and their square values 
"""

number = int(input("Enter the number: "))
print("number-square ")
for index in range (1, number+1):
    square = index**2
    print(f"     {index}-{square} ")
