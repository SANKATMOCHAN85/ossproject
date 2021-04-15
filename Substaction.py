# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
result = float(num1) - float(num2)

# Display the sum
print('The substaction of {0} and {1} is {2}'.format(num1, num2, result))

condition = input('Do you want to substract another number, YES or NO? ')
while condition.upper() == 'YES':
    num3 = input('Enter number: ')
    if float(num3) > result:
        result = float(num3) - result
    else:
        result = result - float(num3)
    condition = input('Do you want to substract another number, YES or NO? ')

print('The substraction of all the numbers results to {0}'.format(result))