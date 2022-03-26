def valid(x, y):
    if int(n) > x >= 0 and int(m) > y >= 0:
        return True
    
    return False


def office(n, m, color):
    desks = []
    deputies = []
    factorsX = [1, -1, 0, 0]
    factorsY = [0, 0, 1, -1]
    
    for i in range(n):
        desks.append(input())
        
    
    for i in range(n):
        for j in range(m):
            if desks[i][j] == color:
                for k in range(4):
                    x = i + factorsX[k]
                    y = j + factorsY[k]
                    
                    if valid(x, y) and desks[x][y] != color and desks[x][y] != '.':
                        deputies.append(desks[x][y])
                        
    
    return len(set(deputies))


n, m, color = input().split()
print(office(int(n), int(m), color))