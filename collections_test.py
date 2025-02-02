from collections import deque

q = deque(maxlen=3)

q.append(1)
q.append(3)
q.append(8)

print(q)

q.extendleft([9])
print(q)

q.popleft()

print(q)
