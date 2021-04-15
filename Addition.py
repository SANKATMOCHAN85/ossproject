# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

condition = input('Do you want to add more numbers, YES or NO? ')
while condition.upper() == 'YES':
    num3 = input('Enter the next number: ')
    sum = float(num3) + sum
    condition = input('Do you want to add more numbers, YES or NO? ')

print('The sum is {0}'.format(sum))
