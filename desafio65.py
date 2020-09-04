high = -999
low = 999
count = 0
sum = 0
answer = 'Y'
while answer in 'Yy':
    num = int(input('Enter a number: '))
    sum += num
    count += 1
    if num > high:
        high = num
    if num < low:
        low = num
    answer = str(input('Enter other number [ Y / N ]: ')).upper().strip()[0]
average = sum / count
print('You entered {} number and average is {}'.format(count, average))
print('High number is {} and Low number is {}'.format(high, low))