






n_changed = int(input('Enter your number(no spaces): '))



num_left = n_changed - 1


original_n = n_changed


while num_left > 0:
    
    n_inputed = n_inputed * num_left
    num_left -= 1
    
print('!' + str(original_n) + ' is equal to ' + str(n_changed))
