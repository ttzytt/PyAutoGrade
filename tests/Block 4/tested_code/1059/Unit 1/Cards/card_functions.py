



def deal_3_hands(deck):
	deck_position = 0
	hands = [[], [], []]
	
	while deck_position < len(deck):
		hands[0].append(deck[deck_position])
		if deck_position + 1 < len(deck):
			hands[1].append(deck[deck_position+1])
		if deck_position + 2 < len(deck):
			hands[2].append(deck[deck_position+2])
		deck_position += 3
	
	return hands


def uno_who_played_what(cards_played):
    card_played_position = 0
    player_position = 100000
    hands = [[], [], [], []]
    skip_1 = 0
    reverse_count = 0

    while card_played_position < len(cards_played):
        if skip_1 == 1:
            player_position += 1
            skip_1 = 0
            if reverse_count % 2 == 1:
                player_position -= 4
        elif cards_played[card_played_position] == "skip":
            skip_1 = 1
            hands[(player_position % 4)].append("skip")
            card_played_position += 1
            player_position += 1
        elif cards_played[card_played_position] == 'reverse':
            reverse_count += 1
            hands[(player_position % 4)].append("reverse")
            card_played_position += 1
            if reverse_count % 2 == 1:
                player_position -= 1
            else:
                player_position += 1
        else:
            hands[(player_position % 4)].append(cards_played[card_played_position])
            card_played_position += 1
            player_position += 1
            if reverse_count % 2 == 1:
                player_position -= 2
    
    return hands

