#배열

# N = int(input())  # 몇 번째 큰 수를 찾을지 입력
# numbers = []

# for _ in range(N):
#     numbers.extend(map(int, input().split()))

# numbers.sort(reverse=True)
# print(numbers[N-1])

N = int(input())

for i in range(N):
    l = list(map(int,input().split()))

cnt = 0
max = 0

for i in range(N-1, 0, -1):
    for j in range(N-1, 0, -1):
        if l[i][j] > max :
            max = l[i][j]
            cnt += 1
        if cnt == max:
            print(l[i][j])
            break