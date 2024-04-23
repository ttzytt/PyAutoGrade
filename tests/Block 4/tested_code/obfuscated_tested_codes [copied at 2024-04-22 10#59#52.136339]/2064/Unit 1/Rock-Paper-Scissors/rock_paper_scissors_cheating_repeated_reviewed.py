



import random

random.seed()

user_choice = input('Enter \'rock\' \'paper\' or \'scissors\': ')

while((user_choice.lower() == 'rock') or
       (user_choice.lower() == 'paper') or
       (user_choice.lower() == 'scissors')):
    

    cheat_or_not_cheat = random.randint(1,10) 
        
    if(cheat_or_not_cheat == 1):
        if (user_choice == 'rock'):
            
            rps_choice = 'paper'
            print('I choose ' + rps_choice + ' I win!')
        elif (user_choice == 'paper'):
            
            rps_choice = 'scissors'
            print('I choose ' + rps_choice + ' I win!')
        elif (user_choice == 'scissors'):
            
            rps_choice = 'rock'
            print('I choose ' + rps_choice + ' I win!')

    else:

        computer_rps_choice = random.choice(['rock', 'paper', 'scissors'])

        if ((user_choice.lower() == 'rock') or
       (user_choice.lower() == 'paper') or
       (user_choice.lower() == 'scissors')):
            
            if(user_choice == computer_rps_choice):
                
                print('I played ' + computer_rps_choice + '! Draw!')
            elif((computer_rps_choice =='rock' and user_choice == 'scissors') or
                 (computer_rps_choice =='scissors' and user_choice == 'paper') or
                 (computer_rps_choice =='paper' and user_choice == 'rock')):
                
                print('I played ' + computer_rps_choice + '! I win!')
                
            else: 
                print('I played ' + computer_rps_choice + '! You win! Good game!')

    user_choice = input('Enter \'rock\' \'paper\' or \'scissors\': ')


print('''You have angered the supreme all-mighty being of doom. Prepare to face
the vengence of the mighty Meowthra!!
    ⠀⡤⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⢤⠀
    ⠀⠈⢧⡀⠉⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠉⢀⣴⠃⠀
    ⠀⠀⠈⠻⡢⡀⠀⠀⡁⠢⠐⠒⠀⠉⠉⠉⠉⠁⠒⠒⠔⠊⠀⠀⢀⠔⠕⠁⠀⠀
    ⠀⠀⠀⠀⠈⢺⢆⢰⡟⠁⠀⠀⠀⣴⡴⢢⣦⠀⠀⠀⠀⠀⠀⠰⡧⠃⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⠘⠋⠀⠀⠀⠀⠀⠁⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⠎⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠱⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡜⢻⠍⠀⣀⡀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⢀⣀⠀⠨⡿⢳⠀⠀⠀⠀
    ⠀⠀⠀⠀⢇⠀⠀⠀⠰⣌⠓⣲⠄⠀⠇⠘⡀⠠⣖⠘⣁⠜⠀⠀⠁⢸⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⠀⠀⠑⢄⡀⠀⢀⡠⠊⣀⣀⠑⢄⡀⠀⢀⡠⠚⠁⠀⡇⠀⠀⠀⠀
    ⠀⠀⠀⢀⠊⠀⠀⢀⡀⠬⡵⢧⠀⠈⣳⣟⠋⠀⡜⢾⠥⠀⣀⠀⠀⠘⡄⠀⠀⠀
    ⠀⠀⡰⠃⠀⠔⠊⠀⡤⠒⠹⣍⠐⠈⠓⠒⠉⢢⢉⠟⠒⢠⡀⠁⠢⠀⠈⢢⠀⠀
    ⠀⠜⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠈⠉⠀⠂⠈⠁⠀⠀⠀⠀⠙⡄⠀⠀⠀⠀⠱⡀
    ⡜⠀⢠⡖⠤⢴⠆⠤⠄⠠⠠⠄⠠⠤⠀⠴⠠⠄⠤⠤⠤⠤⠦⠆⠀⠀⠤⠀⠀⠱

Wow, you suck.

    ⠀⢰⠲⢄⡀⠀⠀⠀⠀⠀⡏⠒⠤⡀⠀⠀⠀⠀⠀⠀
    ⠀⠘⡄⣀⠙⣦⠀⠀⣀⣰⡣⢸⠢⡈⠢⡀⠀⠀⠀⠀
    ⠀⠀⠸⡰⡰⠈⠉⠉⠀⠀⠀⠈⠑⠰⡀⠘⡄⠀⠀⠀
    ⠀⠀⢸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀
    ⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀
    ⢀⣾⡀⢳⢤⣀⠤⠀⠀⠀⢠⣀⣀⡀⠔⠀⠀⣸⠀⠀
    ⠘⢦⡀⡎⠀⡼⠁⠀⢻⠃⠀⠸⡄⠀⡅⠀⠈⢽⠀⠀
    ⠀⠀⠙⠤⣰⠃⠀⠀⠁⡖⠒⢼⡀⠐⣄⠤⠋⠁⠀⠀
    ⠀⠀⠀⠀⢀⡝⠒⡆⠀⠘⡄⠀⠻⣫⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⠊⣀⡼⠀⠀⠀⠈⠢⢀⡠⠃⠀⠀⡰⠊⢱
    ⠀⠀⠀⠀⠉⠀⡇⠀⠀⠀⠀⠀⠀⡇⠀⡠⠊⣠⠔⠁
    ⠀⠀⠀⠀⠀⢸⠀⢤⠤⠤⠤⢤⠄⡯⠓⠋⠉⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⡠⠇⠀⠀⠀⠈⢆⠇⠀⠀⠀⠀⠀⠀
    ''')
