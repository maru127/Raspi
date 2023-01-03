n = int(input('숫자를 입력하세요 : '))
sum = 0
for i in range(1,n+1,1):
    print(i)
    if i % 2 == 0:
        sum = sum + i

print(sum)