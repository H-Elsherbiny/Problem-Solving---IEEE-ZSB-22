def sum_of_digits(n, counter):
    if len(n) == 1:
        return counter
    
    _sum = 0
    counter += 1
    
    for i in n:
        _sum += int(i)
        
    return sum_of_digits(str(_sum), counter)


num = input()
counter = 0
print(sum_of_digits(num, counter))