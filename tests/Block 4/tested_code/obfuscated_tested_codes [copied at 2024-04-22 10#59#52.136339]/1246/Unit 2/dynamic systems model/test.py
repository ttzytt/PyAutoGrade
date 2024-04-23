Romeo_new_love = 0
Juliet_new_love = 0

status_list_romeo = []
status_list_juliet = []
list_diff = []

num_trial = int(input("Days to run: "))
Romeo_love = int(input("Romeos starting love: "))
Juliet_love = int(input("Juliets starting love: "))

for i in range(num_trial):
    Romeo_new_love = Romeo_love + 0.4 * Juliet_love
    Juliet_new_love = Juliet_love - 0.2 * Romeo_love

    Romeo_love = Romeo_new_love
    Juliet_love = Juliet_new_love

    status_list_romeo.append((i, Romeo_love))
    status_list_juliet.append((i, Juliet_love))
    
    list_diff.append((i, abs(Romeo_love - Juliet_love)))
print(status_list_romeo)
print(status_list_juliet)
print(list_diff)
