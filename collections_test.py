from collections import deque
import heapq

q = deque(maxlen=3)

q.append(1)
q.append(3)
q.append(8)

# print(q)

q.extendleft([9])
# print(q)

q.popleft()

# print(q)

nums = [2, 5, -8, 89, 19, 22]

change = list(nums)
print("First One", change)
heapq.heapify(change)
heapq.heappush(-22, change)

print(change)


smallest = heapq.nlargest(3, nums)
# print(smallest)




