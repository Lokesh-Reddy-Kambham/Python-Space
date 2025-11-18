#version 1
n1 = int(input("Enter a Number:"))
n2 = int(input("Enter a Number:"))
n3 = int(input("Enter a Number:"))
if n1>n2:
    if n1>n3:
        print(f"{n1} is Greater")
    elif n1==n3:
        print(f"{n1} and {n3} are Equal and Greater than {n2}")
    else:
        print(f"{n3} is Greater")
elif n2>n3:
    if n2==n1:
        print(f"{n2} and {n1} are Equal and Greater than {n3}")
    else:
        print(f"{n2} is Greater")
elif n3>n1:
    if n3==n2:
        print(f"{n3} and {n2} are Equal and Greater than {n1}")
    else:
        print(f"{n3} is Greater")
else:
    print("All are Equal")

#version 2
n1 = int(input("Enter a Number:"))
n2 = int(input("Enter a Number:"))
n3 = int(input("Enter a Number:"))
if n1==n2 and n2==n3:
    print("All are Equal")
elif n1>=n2 or n1>=n3:
    if n1==n2:
        print(f"{n1} and {n2} are Equal and Greater than {n3}")
    elif n1==n3:
        print(f"{n1} and {n3} are Equal and Greater than {n2}")
    else:
        print(f"{n1} is Greater")
elif n2>=n3 or n2>=n1:
    if n2==n3:
        print(f"{n2} and {n3} are Equal and Greater than {n1}")
    elif n2==n1:
        print(f"{n2} and {n1} are Equal and Greater than {n3}")
    else:
        print(f"{n2} is Greater")
else:
    print(f"{n3} is Greater")