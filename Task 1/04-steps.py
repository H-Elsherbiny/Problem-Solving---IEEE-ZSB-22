def steps():
    yard = list(map(int, input().split()))
    position = list(map(int, input().split()))
    n = int(input())
    
    counter = 0
    for i in range(n):
        vector = list(map(int, input().split()))
        
        temp = []
        for j in range(2):
            if vector[j] > 0:
                temp.append((yard[j] - position[j]) // vector[j])
                
            elif vector[j] < 0:
                temp.append((position[j] - 1) // abs(vector[j]))
            
            else:
                temp.append(float('inf'))
                
        distance = min(temp)
        counter += distance
        
        position[0] += distance * vector[0]
        position[1] += distance * vector[1]
        
            
    return counter


print(steps())