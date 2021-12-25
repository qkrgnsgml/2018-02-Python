import random
i = 0
counters = [0, 0, 0, 0, 0, 0]
while True:
    value = random.randint(0, 5)
    counters[value] = counters[value] + 1
    i = i + 1

    if i == 1000:
        break

a = 0
while a < 6:
    print('주사위 {0}의 횟수는 {1}입니다.'.format(a+1,counters[a]))
    a = a + 1

