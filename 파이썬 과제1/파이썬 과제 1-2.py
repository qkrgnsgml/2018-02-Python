import random
count = 0
while count < 3:
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    print('첫 번째 주사위 : {0}    두 번째 주사위 : {1}' .format(r1,r2))
    count = count + 1
