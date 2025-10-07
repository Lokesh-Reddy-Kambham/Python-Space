num = int(input("Enter a number:"))
n1 = 0
n2 = 1
counter = 0
while counter < num:
    print(n1 ,end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    counter += 1

print()

m1 = 0
m2 = 1
for i in range(num):
    print(m1,end=" ")
    m3 = m1 + m2
    m1 = m2
    m2 = m3