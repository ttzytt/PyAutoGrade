






number_n = int(input("Please type in your n: "))


number_minus_1 = number_n - 1






while number_minus_1 > 1:

    number_n = number_n * number_minus_1
    number_minus_1 = number_minus_1 - 1
print("Your factorial number is " + str(number_n))


