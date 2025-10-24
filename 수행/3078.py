#큐

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()               # 윈도우를 유지할 큐
count_len = [0] * 21      # 길이별 학생 수 카운트
ans = 0

for _ in range(N):
    l = len(input().rstrip())
    
    # 현재 윈도우 안 동일 길이 학생 수만큼 좋은 친구 쌍 추가
    ans += count_len[l]
    
    # 새 학생 추가
    q.append(l)
    count_len[l] += 1
    
    # 윈도우 범위 초과 시 가장 오래된 학생 제거
    if len(q) > K:
        old = q.popleft()
        count_len[old] -= 1

print(ans)