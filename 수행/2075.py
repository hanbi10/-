#배열

N = int(input())  # 몇 번째 큰 수를 찾을지 입력
numbers = []

for _ in range(N):
    numbers.extend(map(int, input().split()))

numbers.sort(reverse=True)
print(numbers[N-1])