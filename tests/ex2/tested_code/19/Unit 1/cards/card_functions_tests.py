from card_functions import uno_who_played_what



results1 = uno_who_played_what(['1', '2', '3', '4', '5', 'skip', '7'])
print(results1)


results2 = uno_who_played_what(['reverse', 'skip', '0', '1', '2', '3', 'reverse', '4'])
print(results2)


results3 = uno_who_played_what(['1', '2', '3', '4', 'skip', 'reverse', '7', '8', '9'])
print(results3)


results4 = uno_who_played_what(['skip', 'reverse', '0', '1', 'reverse', '2', '3', '4', '5'])
print(results4)


results5 = uno_who_played_what(['reverse', 'skip', 'reverse', '1', '2', '3', '4', '5', 'skip', '6'])
print(results5)

