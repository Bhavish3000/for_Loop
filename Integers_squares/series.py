"""This program prints the number series in 10,20,30,40,...300.

"""
number = int(input("Enter the number:"))
INDEX =1
while INDEX <=number:
    SEQUENCE = INDEX*10
    print(f"{SEQUENCE},",end=' ')
    INDEX +=1
