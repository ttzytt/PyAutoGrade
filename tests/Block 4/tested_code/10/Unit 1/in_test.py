


pets = ['dog', 'cat', 'mouse', 'snake', 'fish']
new_pets = ['pig', 'dog', 'mouse', 'turtle']

for pet in new_pets:
    if pet not in pets:
        pets.append(pet)

print(pets)
        
