


''' 
 This program is written for aircraft landing in different weathers
 Most commercial aircrafts are not designed to handle windsheer, 
 but are able to land when the windsheer is less than 11 degrees.
 When the wind speed is less than 30 knots, the planes are able to land.
 Landing requires ILS or visual on the run way.
'''


Windsheer = input("Is there windsheer? Input Yes or No ")


if(Windsheer == "Yes"):
    wind_sheer_degree=int(input("How many degrees of windsheer does the runway have? "))
    if wind_sheer_degree > 11:
        print("Please climb to a higher attitude and try a different airport")
    if wind_sheer_degree <= 11:
		
		
	
        wind_speed = int(input("How many knots of wind do you have? "))
        if wind_speed <= 30:
            visual = input("Do you have a visibility more than 6 km? Yes Or No ")
            
            if visual == "Yes":
                print("Have a safe landing")
            else:
                ILS = input("Do you have ILS? Yes Or No ")
                if ILS == "Yes":
                    print("Have a safe landing")
                else:
                    print("Contact tower for ILS, hold or go to different airport")
                           
        if wind_speed >30:
                            print("Try again at a different time or location")
                            
                            


if(Windsheer == "No"):        
    wind_speed = int(input("How many knots of wind do you have? "))
    if wind_speed <= 30:
        visual = input("Do you have a visibility more than 6 km? Yes Or No ")
        if visual == "Yes":
            print("Have a safe landing")
        else:
            ILS = input("Do you have ILS? Yes Or No ")
            if ILS == "Yes":
                print("Have a safe landing")
            else:
                print("Contact tower for ILS support, hold or go to different airport")
                           
    if wind_speed >30:
                        print("Try again at a different time or location")
                            
                            

                        


    
