




def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def triangular_number(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def new_triangular_number(n):
    total = 0
    start = 1 if n % 2 == 1 else 2
    for i in range(start, n + 1, 2):
        total += i
    return total

if __name__ == "__main__":
    
    num = int(input("Enter an integer: "))

    
    fact_result = factorial(num)
    triangular_result = triangular_number(num)
    new_triangular_result = new_triangular_number(num)

    
    print(f"{num}! is {fact_result}")
    print(f"Triangular number: {triangular_result}")
    print(f'"{new_triangular_result}" triangular number: {new_triangular_result}')
