pets = ['dog', 'cat', 'mouse', 'snake', 'fish']
new_pets = ['pig', 'dog', 'mouse', 'turtle']

for new_pet in new_pets:
    if new_pet not in pets:
        pets.append(new_pet)
print(pets)
