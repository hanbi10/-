#배열

numbers = []  # 모든 입력 숫자를 담을 빈 리스트 초기화

for _ in range(N):  # N개의 줄을 반복
    numbers.extend(map(int, input().split()))  


numbers.sort(reverse=True)  


print(numbers[N-1])  
