



n_final_ans = int(input('Enter your number(no spaces): '))


n_left = n_final_ans - 1


n_original = n_final_ans


while n_left > 0:
    n_final_ans += n_left
    n_left -= 1


print('The triangle number of ' + str(n_original) + ' is ' + str(n_final_ans))

