



price = 0
tag = float(input('Enter the price on the tag: '))
while tag != -1.00:
 tax = input('Is it tax free? ')
 if tax == '1':
  price = price + tag
 elif tax == '0':
  price = price + (tag*1.06625)
 print(price)
 print()
 tag = float(input('Enter the price on the tag: '))
if tag == -1.00:
 print('Your total price is $' + str((round(price*100))/100))




