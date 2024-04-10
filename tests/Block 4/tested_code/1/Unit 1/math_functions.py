
def factorial_number(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


def triangular_number(n):
    return n * (n + 1) // 2


def new_triangular_number(n):
    if n % 2 == 0:
        return n * (n // 2)
    else:
        return ((n + 1) // 2) ** 2


user_input = int(input("Enter an integer: "))


factorial_result = factorial_number(user_input)
triangular_result = triangular_number(user_input)
new_triangular_result = new_triangular_number(user_input)


print(f"{user_input}! is {factorial_result}")
print(f"Triangular number: {triangular_result}")
print(f'"New" triangular number: {new_triangular_result}')
