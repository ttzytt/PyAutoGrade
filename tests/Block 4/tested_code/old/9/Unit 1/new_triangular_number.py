




print('We typically prefer using a loop')
print('to calculate for triangular number.')
print('However, there could be other ways')
print('to solve this problem, so let\'s')
print('try it out!')
print()
print('Also, this isn\'t actually my idea,')
print('I got this from Einstein, but it\'s')
print('still interesting to know how it works')
print()

# Define input
def outcome(client):
    if client % 2 == 0: # Client is even number
     return client*(client+1)/2
    elif client % 2 == 1: # Client is odd number
     client = client - 1 # Turning it into even number so it's simpler
     return (client+2)*(client+1)/2
    
    
    


client = int(input('Enter an integral: '))
print()
print('The triangular number of your input is:')
print(outcome(client))


