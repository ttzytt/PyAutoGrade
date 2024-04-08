


n = int(input("Please enter an interger: "))

def triangular_number(n):
    count = 1 
    triangular_number = 0 

    
    while count <= n:
        triangular_number = triangular_number + count
        count = count + 1
    return triangular_number


def even_new_triangular_number(n):
    return (triangular_number(n) + n / 2) / 2



def new_triangular_number(n):
    if n / 2 == round(n / 2):
        return even_new_triangular_number(n)
    else:
        return triangular_number(n) - even_new_triangular_number(n-1)


print('"New" triangular number: ' + str(round(new_triangular_number(n))))

    


    
    
