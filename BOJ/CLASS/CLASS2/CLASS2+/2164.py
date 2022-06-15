# 카드 2

# deque 구현하는 문제
# 예전엔 deque를 몰라서 못풀었음 ㅋㅋㅋ

from collections import deque

N = int(input())

queue = deque([x for x in range(1, N+1)])

while len(queue) >= 2:

    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])