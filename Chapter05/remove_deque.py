import collections

doubleEndedQueue = collections.deque('123456')

print("Deque: {}".format(doubleEndedQueue))

# Removing Elements from our array
rightPop = doubleEndedQueue.pop()
print(rightPop)
print("Deque: {}".format(doubleEndedQueue))

leftPop = doubleEndedQueue.popleft()
print(leftPop)
print("Deque: {}".format(doubleEndedQueue))
