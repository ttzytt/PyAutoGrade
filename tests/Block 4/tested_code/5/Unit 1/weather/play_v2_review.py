

temperature = int(input('What is the temperature today (in °F)?'))
rain = input('Is it raining today?')


if temperature < 32:
    print("It's too cold outside!")
elif temperature > 95:
    print("It's too hot outside!")


elif rain == ('yes'):
    jacket = input("Do you have a jacket?")
    if jacket == ('no'):
        print("You should not go outside.")
    if jacket == ('yes'):
        print("You can go outside but it might be wet.")


elif rain == ('no'):
    if temperature >= 32 or temperature <= 50:
        print("You can go outside.")
    elif temperature > 50 or temperature <= 95:
        print("You should play outside today.")
                
    
            
 

        




                
