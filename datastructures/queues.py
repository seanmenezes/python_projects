# you can use list to implement queue however for large lists removing 1 item from start results
# in all items moving one space which is a performance issue
# better option use deque
# import dequeue from collections module. module is a bucket with a bunch of reusable code.
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)
# use deque method remove item from the begining of the queue
queue.popleft()
print(queue)
# queue is empty
if not queue:
    print("empty")
