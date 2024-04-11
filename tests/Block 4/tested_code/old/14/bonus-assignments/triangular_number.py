









def validate_int(num):
    
    try:
        int(num)
    
    except:
        print("You didn't enter an integer >:(")
        return False
    else:
        
        if int(num) >= 1:
            return True
        
        else:
            print("That's not positive >:OOO")
            print("Enter a positive integer...")
            return False


valid_input = False
while not valid_input:
    num = input("Give a positive integer:  ")
    
    valid_input = validate_int(num)



i = 1
total_sum = 0
while i <= int(num):
    total_sum += i 
    i += 1 


suffixes = {
    1: "st",
    2: "nd",
    3: "rd"
    }
suffix = suffixes.get(num, "th") 

print(f"The {num}{suffix} triangular number is equal to {total_sum}.")

