
bs = ['a','b','c','d','e']
new_bs = ['f','a','c','o']

for b in bs:
    if b not in new_bs:
        new_bs.append(b)
    print(new_bs)
    
