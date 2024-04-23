



cereal_key = {'purple':4, 'blue':5, 'red':6, 'green':6, 'yellow':7, 'orange':7}
user_input = input("What color(s) do you want to count? ('quit' to quit)")
targets = user_input.split()

while user_input != 'quit':
    total_count = 0
    
    for color in range(len(targets)):
        if targets[color] in cereal_key:
            total_count += cereal_key[targets[color]]   
        else:
            print("You bozo, there ain't no " + targets[color] + " colored fruit loops.")
            color = len(targets)
    print('There are ' + str(total_count) + ' fruit loops with those colors.') 
            
    user_input = input('What colors do you want to count? ')
    targets = user_input.split()
    
print("Sad to see you go ˙◠˙")
