num = int(input("Enter a Number:"))
reverse_number = str(num)[::-1]
reversal = 0
while num>0:
    remainder = num % 10
    num = num // 10
    reversal =  reversal*10 + remainder
print(reversal)

print(int(reverse_number))
