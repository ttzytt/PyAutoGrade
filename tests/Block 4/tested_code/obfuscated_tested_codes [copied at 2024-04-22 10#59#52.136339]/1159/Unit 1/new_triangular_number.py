




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

"""
For those of you who are wondering how this program works,
it's a good idea to see how Einstein used to solve this problem:

For even numbers, let's make an example for client = 6:
In order to compute 6+5+4+3+2+1, we can first observe that 6+1 = 5+2 = 4+3,
which means there are many pair of numbers that have same value as client+1,
and there are client/2 pairs for total, as such we can multiply client+1 by
client/2, and we get the final result client*(client+1)/2

For odd numbers, let's make an example for client = 5:
This case is a bit more complex than even number, because we can't find pairs in
odd numbers, so we subtract the original input by 1,
now we have client = client-1 and we get an even number,
with an even number, we can follow the same process above, and we now get
client*(client+1)/2, however, since we initially substracted the input, now we have
to get it back, so we add client+1 (the client now isn't the client that we input!)
into client*(client+1)/2, which is (client+2)*(client+1)/2 the final result

Einstein was asked to solve 1+2+3...+99+100, his calculation was
100*(100+1)/2 = 50*101 = 5050, you can try it out in this program

The above text is the explanations, I hope it's helpful for you!

"""
