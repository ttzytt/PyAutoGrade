from card_functions import deal_3_hands

def test_deal_3_hands():
    deck = [1, 2, 3, 4, 5, 6, 7]
    hands = deal_3_hands(deck)
    
    assert hands == [[1, 4, 7], [2, 5], [3, 6]], "Test Case 1 Failed"
    
    deck = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    hands = deal_3_hands(deck)
    
    assert hands == [['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I']], "Test Case 2 Failed"
    
    

if __name__ == '__main__':
    test_deal_3_hands()
    print("All tests passed!")


from card_functions import uno_who_played_what

def test_uno_who_played_what():
    cards_played = ['1', '2', '3', '4', '5', 'skip', '7']
    result = uno_who_played_what(cards_played)
    expected = [['Player 1', '1', '5'], ['Player 2', '2', 'skip'], ['Player 3', '3'], ['Player 4', '4', '7']]
    
    assert result == expected, "Test Case 1 Failed"

    cards_played = ['0', 'reverse', 'skip', '9', 'skip', '2', '4', 'skip', '8', '1', 'reverse', '6', '3', 'skip', '7', '5']
    result = uno_who_played_what(cards_played)
    expected = [
        ['Player 1', '0', 'skip', 'skip', 'reverse'],
        ['Player 2', 'reverse', '9', '8', 'reverse'],
        ['Player 3', '4', '2', '1', '3'],
        ['Player 4', '7', '5', '6']
    ]
    
    assert result == expected, "Test Case 2 Failed"

if __name__ == '__main__':
    test_uno_who_played_what()
    print("All tests passed!")
from card_functions import uno_who_played_what

def test_uno_who_played_what():
    cards_played = ['1', '2', '3', '4', '5', 'skip', '7']
    result = uno_who_played_what(cards_played)
    expected = [['Player 1', '1', '5'], ['Player 2', '2', 'skip'], ['Player 3', '3'], ['Player 4', '4', '7']]
    
    assert result == expected, "Test Case 1 Failed"

    cards_played = ['0', 'reverse', 'skip', '9', 'skip', '2', '4', 'skip', '8', '1', 'reverse', '6', '3', 'skip', '7', '5']
    result = uno_who_played_what(cards_played)
    expected = [
        ['Player 1', '0', 'skip', 'skip', 'reverse'],
        ['Player 2', 'reverse', '9', '8', 'reverse'],
        ['Player 3', '4', '2', '1', '3'],
        ['Player 4', '7', '5', '6']
    ]
    
    assert result == expected, "Test Case 2 Failed"

if __name__ == '__main__':
    test_uno_who_played_what()
    print("All tests passed!")
