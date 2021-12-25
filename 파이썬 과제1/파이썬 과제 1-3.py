a = []
hab = 0
count = 0
while count<5:
    print('정수를 입력하세요')
    b = int(input())
    hab = hab + b
    a.append(b)
    count = count + 1
avg = hab / len(a)
print('평균은 {0}입니다'.format(avg))
