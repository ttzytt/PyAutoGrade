'''
YOU MAY RUN THIS PROGRAM

'''



from card_functions import *








def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')




def deal_3_hands_TEST(): 
    print('Start deal_3_hands_TEST')
    
    TEST(deal_3_hands([1,2,3,4,5,6]) == [[1,4],[2,5],[3,6]])
    TEST(deal_3_hands([1,3,4,2,3,8,3,1]) == [[1,2,3],[3,3,1],[4,8]])
    TEST(deal_3_hands([1,5,3,2,5,4,6]) == [[1,2,6],[5,5],[3,4]])
    
    (TEST(deal_3_hands(['I','LOVE','YOU','MY','DEAR','WIFE'])
         == [['I','MY'],['LOVE','DEAR'],['YOU','WIFE']]))
    (TEST(deal_3_hands(['A','B','C','D','E','F','G'])
          == [['A','D','G'],['B','E'],['C','F']]))
    print('End deal_3_hands_TEST')
    print()


def uno_who_played_what_TEST(): 
    print('Start uno_who_played_what_TEST')

    (TEST(uno_who_played_what(['1','2','3','4','5','6','7','8'])
          == [['1','5'],['2','6'],['3','7'],['4','8']])) 

    (TEST(uno_who_played_what(['1','2','3','4','5','skip','6'])
          == [['1','5'],['2','skip'],['3'],['4','6']])) 
    
    (TEST(uno_who_played_what(['1','2','3','4','5','reverse','6','7'])
          == [['1','5','6'],['2','reverse'],['3'],['4','7']]))
    
    
    (TEST(uno_who_played_what(['1','2','skip','3','4'])
          == [['1','3'],['2','4'],['skip'],[]])) 

    (TEST(uno_who_played_what(['1','2','3','skip','4','reverse','5','6'])
          == [['1','6'],['2','4','5'],['3','reverse'],['skip']]))
    

    (TEST(uno_who_played_what(['1','2','3','reverse','4','5','skip','6'])
          == [['1','skip'],['2','5'],['3','4','6'],['reverse']]))

    (TEST(uno_who_played_what(['1','2','reverse','3','4','reverse','5'])
          == [['1','4','5'],['2','3'],['reverse'],['reverse']]))

    print('End uno_who_played_what_TEST')
    print()


def who_played_how_many_TEST(): 
    print('Start who_played_how_many_TEST')
    (TEST(who_played_how_many(['1','2','3','4','5','6','7','8'])
          == [2,2,2,2]))
    
    (TEST(who_played_how_many(['1','2','3','4','5','skip','6'])
          == [2,2,1,2]))
    
    (TEST(who_played_how_many(['1','2','3','4','5','reverse','6','7'])
          == [3,2,1,2]))

    (TEST(who_played_how_many(['1','2','3','reverse','4','5','skip','6'])
          == [2,2,3,1])) 

    (TEST(who_played_how_many(['1','2','reverse','3','4','reverse','5'])
          == [3,2,1,1]))

    print('End who_played_how_many_TEST')
    print()
    

def uno_who_played_what_2_TEST(): 
    print('Start uno_who_played_what_2_TEST')
    (TEST(uno_who_played_what_2(['1','2','3','4','5','6'],5,2)
          == [['4'],['5'],['1','6'],['2'],['3']]))

    (TEST(uno_who_played_what_2(['1','2','3','skip','4','5','reverse','6','7'],6,3)
          == [['skip'],[],['4','7'],['1','5','6'],['2','reverse'],['3']]))

    (TEST(uno_who_played_what_2(['1','2','3','4','reverse','5','skip','6','reverse','7'],3,2)
          == [['2','reverse'],['3','skip','reverse'],['1','4','5','6','7']]))

    (TEST(uno_who_played_what_2(['1','2','skip','3'],2,0)
          == [['1','skip','3'],['2']]))

    (TEST(uno_who_played_what_2(['1','2','3','skip','reverse','4'],3,1)
          == [['3','reverse'],['1','skip'],['2','4']]))
    print('End uno_who_played_what_2_TEST')
    print()


def catch_cheater_TEST(): 
    print('Start catch_cheater_TEST')
    (TEST(catch_cheater((['red','1'],['blue','1'],['blue','7'],['blue','9'],
                       ['red','6']),['yellow','1'],4,0)
          == 0))
    (TEST(catch_cheater((['red','1'],['blue','1'],['blue','7'],['blue','9'],
                       ['red','9'],['yellow','3']),['yellow','1'],4,0)
          == 1))
    (TEST(catch_cheater((['red','1'],['blue','1'],['blue','7'],['green','7'],
                       ['green','skip'],['blue','2']),['yellow','1'],5,0)
          == 1))
    (TEST(catch_cheater((['red','1'],['blue','1'],['blue','7'],['green','7'],
                       ['green','skip'],['blue','2']),['yellow','1'],6,2)
          == 2))
    (TEST(catch_cheater((['red','1'],['blue','1'],['blue','7'],['green','7'],
                       ['green','reverse'],['blue','2']),['yellow','1'],3,0)
          == 0))
    print('Start catch_cheater_TEST')
    print()

    






deal_3_hands_TEST()
uno_who_played_what_TEST()
who_played_how_many_TEST()
uno_who_played_what_2_TEST()
catch_cheater_TEST()


'''
Bonus part: coming soon
'''









'''
This type of comments (green) is special comments
It's function is for acknowledgements and reminder for my self
Reviewer need not pay attention to green comments

'''



