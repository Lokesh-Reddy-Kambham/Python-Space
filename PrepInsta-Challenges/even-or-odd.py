#version 1
num = int(input("Enter Number:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

#version 2
num = int(input("Enter Number:"))
print("Even Number" if num%2==0 else "Odd Number")

#version 3
num = int(input("Enter Number:"))
result = ["Even Number","Odd Number"]
print(result[num%2])