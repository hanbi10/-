import sys
from collections import deque

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())              # 학생 수 N, 등수 차이 허용 K
    q = deque()                                    # 현재 윈도우(큐)에 이름길이들을 담을 큐
    count_len = [0] * 21                           # 이름 길이가 0~20인 경우를 담을 카운트 배열
    ans = 0                                        # 좋은 친구 쌍의 개수를 저장할 변수
    
    # 처음 K명까지 큐에 넣고 카운트만 처리 (등수 차이 ≤ K 조건을 준비)
    for _ in range(K):
        l = len(input().rstrip())                  # 학생 이름의 길이
        ans += count_len[l]                        # 현재 길이 l와 동일한 이전 윈도우 내 학생 수만큼 좋은 친구 쌍 추가
        count_len[l] += 1                           # 길이 l 학생 1명 추가
        q.append(l)                                 # 큐에도 길이 l 추가
    
    # 나머지 학생들을 처리하면서, 큐(윈도우)를 앞에서 하나 뺴고 뒤에서 하나 추가하는 방식
    for _ in range(N - K):
        l = len(input().rstrip())                  # 새 학생 이름의 길이
        ans += count_len[l]                        # 윈도우 내 동일한 길이 학생 수만큼 좋은 친구 추가
        count_len[l] += 1                           # 새 학생 길이 카운트 증가
        q.append(l)                                 # 새 학생 길이를 큐에 추가
        
        old = q.popleft()                           # 윈도우에서 범위 벗어나는 학생 길이
        count_len[old] -= 1                         # 그 학생 길이 카운트에서 제거
    
    print(ans)                                     # 결과 출력

if __name__ == "__main__":
    main()