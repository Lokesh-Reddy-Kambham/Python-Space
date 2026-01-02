#1  my approach
array = [3,5,6,99,23,78,1,9,99]
maximum = second = array[0]
for i in array:
    if i > maximum :
        maximum = i
print(maximum,array.index(maximum))
for j in array:
    if j!= maximum and j>second:
        second = j
print(second,array.index(second))

#2 interview approach
array = [3,5,6,99,23,78,1,9,99]
largest = array[0]
if len(array)<2:
    print("not found second largest")
else :
    largest = second = float("-inf")
    for i in array:
        if i > largest:
            second = largest
            largest = i
        elif i != largest and i > second :
            second = i
    if second == float("-inf"):
        print("second not exist")
    else:
        print(second)