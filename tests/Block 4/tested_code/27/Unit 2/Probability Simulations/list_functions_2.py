





def largest_element(numbers):
        
	numbers.sort()
	return (numbers[-1])


def alternate_sum(numbers):
	return(sum(numbers[0:len(numbers):2]) - sum(numbers[1:len(numbers):2]))



def rotate_right(numbers):
        
	return ([numbers[-1]] + numbers[0:-1])


def deal_3_hands(numbers):
        
	return ([[(numbers[0:len(numbers):3])], [(numbers[1:len(numbers):3])], [(numbers[2:len(numbers):3])]])
if len(numbers)>0:
        

