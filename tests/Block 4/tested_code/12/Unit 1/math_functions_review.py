



def factorial(player_number):
    factorial = player_number
    
    while player_number > 1:
        factorial = factorial * (player_number - 1)
        player_number = player_number-1
    return(factorial)


def triangular(player_number):
    triangular = player_number
    
    while player_number > 1:
        triangular = triangular + (player_number - 1)
        player_number = player_number - 1
    return(triangular)


def new_triangular(player_number):
    new_triangular = player_number
    
    if player_number % 2 == 0:
        
        while player_number > 2:
            new_triangular = new_triangular + (player_number - 2)
            player_number = player_number - 2
    else:
        
        while player_number > 1:
            new_triangular = new_triangular + (player_number - 2)
            player_number = player_number - 2
    return(new_triangular)
    


player_number = int(input("Enter a number: "))

print(str(player_number) + '! is ' + str(factorial(player_number)))
print("Triangular number: " + str(triangular(player_number)))
print('"New" triangular number: ' + str(new_triangular(player_number)))


