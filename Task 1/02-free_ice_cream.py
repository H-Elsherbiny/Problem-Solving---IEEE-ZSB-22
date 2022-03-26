def ice_cream():
    
    n, d = map(int, input().split())
    counter = 0
    
    for _ in range(n):
        sign, packs = input().split()
        packs = int(packs)
        
        if sign == '+':
            d += packs
            
        else:
            if d >= packs:
                d -= packs
                
            else:
                counter += 1
                
    return d, counter


print(*ice_cream(), sep=(" "))