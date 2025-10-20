n = int(input())               # 만들 수열의 길이 입력받기
stack, ans = [], []            # 스택과 연산결과 저장 리스트 초기화
find = True                    # 수열 생성 가능 여부를 True로 초기화
now = 1                        # 현재 push할 숫자는 1부터 시작

for _ in range(n):             # n개의 숫자를 차례로 입력받음
    num = int(input())         # 현재 만들어야 할 숫자
    
    # 스택에 아직 넣지 않은 숫자를 push
    while now <= num:          
        stack.append(now)      # 스택에 현재 숫자 push
        ans.append('+')        # push 연산 기록
        now += 1               # 다음 숫자로 이동
    
    # 스택의 맨 위 숫자가 현재 숫자와 같다면 pop
    if stack[-1] == num:
        stack.pop()            # 스택에서 pop
        ans.append('-')        # pop 연산 기록
    else:
        find = False           # 수열을 만들 수 없음
        break                  # 반복 종료

# 결과 출력
if not find:                   # 불가능한 경우
    print("NO")
else:                          # 가능한 경우
    for i in ans:              # 모든 연산 순서 출력
        print(i)