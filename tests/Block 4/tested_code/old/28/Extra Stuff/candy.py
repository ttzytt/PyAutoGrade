input_candy = int(input('How much candy? '))

total_sum = 0
candy = 1
output = []

while True: 
    if total_sum + (2*candy + 1) <= input_candy:
        output.append(candy)
        total_sum += candy
    else:
        break
    candy += 1

output.append(input_candy - total_sum)

print(output)
