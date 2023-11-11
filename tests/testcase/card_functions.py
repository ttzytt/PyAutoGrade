from test_case import  PrewrittenFileCase as pf, PrewrittenScriptCase as ps
from test_case import *
import random
from inspect import signature

def correct_solution(cards_played, num_players = 4, player_index = 0):
    
    hands = [[] for _ in range(num_players)]
    
    play_order = 1  # reverse negates this

    for i in range(len(cards_played)):
        hands[player_index].append(cards_played[i])

        if cards_played[i] == 'skip':
            player_index = (player_index + play_order) % num_players
        elif cards_played[i] == 'reverse':
            play_order *= -1

        player_index = (player_index + play_order) % num_players

    return hands

def random_input_test(func):
    random.seed(0)
    INPUT_LEN = 10000
    sig = signature(func)
    param_len = len(sig.parameters)
    possible_cards = [str(i) for i in range(1, 10)] + ['skip', 'reverse']
    cards_played = []
    for i in range(INPUT_LEN):
        cards_played.append(random.choice(possible_cards))
    if param_len == 1:
        expected = correct_solution(cards_played)
    elif param_len == 3:
        expected = correct_solution(cards_played, 4, 0)
    else: 
        raise Exception("the function should have 1 or 3 parameters, but it has {} parameters".format(param_len))
    actual = func(cards_played)
    return ps.EvaluatorResult(
        expected == actual, 
        expected, 
        actual
    )
    
def bonus_question_test(func):
    sig = signature(func)
    param_len = len(sig.parameters)
    if param_len != 3: 
        return ps.EvaluatorResult(False, msg="to implemented the bonus question, you should provide parameters for customizing the number of players and the starting player")
    random.seed(0)
    EACH_ROUND_INPUT_LEN = 500 
    ROUNDS = 500
    NUM_PLAYER_RG = (2, 1000) 
    for r in range(ROUNDS): 
        num_player = random.randint(*NUM_PLAYER_RG)
        player_index = random.randint(0, num_player - 1)
        possible_cards = [str(i) for i in range(1, 10)] + ['skip', 'reverse']
        cards_played = []
        for _ in range(EACH_ROUND_INPUT_LEN):
            cards_played.append(random.choice(possible_cards))
        expected = correct_solution(cards_played, num_player, player_index)
        actual = func(cards_played, num_player, player_index)
        if expected != actual:
            return ps.EvaluatorResult(
                False, 
                expected, 
                actual
            )
    return ps.EvaluatorResult(True)
        
    
def test_case_constructor() -> list[TestCase]:
    peb = ps.EvaluatorBuilder()
    _ps = lambda evaluator, msg = None: ps(evaluator, "uno_who_played_what", msg)
    # here because we only wanted to test one function, so I wrote a wrapper to type less words
    return [
        # the first parameter is the expected value and the second is the input for the tested function
        _ps(peb.assert_eq([['1', '5'], ['2', 'skip'], ['3'], 
                       ['4', '7']], ['1', '2', '3', '4', '5', 'skip', '7' ])), 
        _ps(peb.assert_eq([['1', '5','7'], ['2', 'reverse'], ['3'], ['4']],
                        ['1', '2', '3', '4', '5', 'reverse', '7' ])),
        _ps(peb.assert_eq([['1'], ['2','reverse','7'], ['reverse','5'], ['skip']], 
                        ['1', '2', 'reverse', 'reverse', '5', 'skip', '7'])),
        _ps(peb.assert_eq([['1', '5'], ['2', 'skip'], ['3'],
                          ['4', '7']], ['1', '2', '3', '4', '5', 'skip', '7' ])),
        _ps(random_input_test, "random input test"), 
        _ps(bonus_question_test, "bonus question test")
    ]