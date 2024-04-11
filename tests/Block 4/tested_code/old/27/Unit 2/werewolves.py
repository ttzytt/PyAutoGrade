





import random
random.seed


def find_winner(num_werewolves , num_villagers):
	if num_werewolves > num_villagers:
		return "werewolves"
	day_night = -1
	
	
	while ((num_werewolves != 0) and (num_werewolves != num_villagers)):
		total = num_werewolves + num_villagers
		day_night += 1
		if day_night%2 == 0:	
			kill = random.randint(1, total) 
			if kill <= num_villagers:
				num_villagers -= 1
			else:
				num_werewolves -= 1
		elif day_night%2 == 1:
			
			num_villagers -= 1
	
	if num_werewolves == 0:
		return "villagers"
	
	elif num_werewolves == num_villagers:
		return "werewolves"




def odds_of_werewolves_winning(num_werewolves , num_villagers):
	village_win = 0
	werewolves_win = 0
	repeat = 0
	while repeat < 10000: 
		win = (find_winner(num_werewolves,num_villagers))
		if win == "villagers":
			village_win += 1
		
		elif win == "werewolves":
			werewolves_win += 1
			
		repeat += 1
		total_win = werewolves_win + village_win

	return werewolves_win/total_win

num_werewolves = int(input("How many werewolves: "))
num_villagers = int(input("How many villagers: ")) 


print(odds_of_werewolves_winning(num_werewolves, num_villagers))


