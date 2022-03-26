def Name(name):
    name = [x for x in name]
    name = set(name)
    
    if len(name) % 2 == 0:
        print("CHAT WITH HER!")
        return 0
    
    else:
        print("IGNORE HIM!")
        return 1

n = input()
Name(n)