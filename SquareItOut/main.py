def square(start, end):
    odd = []
    even = []
    for number in range(start,(end+1)):
        square = number * number
        if square%2 == 0:
            even.append(square)
        else:
            odd.append(square)
        return odd,even    
    
start = int(input("Enter starting point of range: "))
end = int(input("Enter ending point of range: "))
print(square(start,end))
