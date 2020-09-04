count = sum = 0
while True:
    num = int(input('Digite um numero [33-STOP]: '))
    if num == 33:
        break
    sum += num
    count += 1

print(f'Entered {count} number and the sum is {sum}.')
