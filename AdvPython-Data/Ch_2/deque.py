# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)
# TODO: deques support the len() function
print(f"Item length = {len(d)}")
# TODO: deques can be iterated over
for elem in d:
    print(elem.upper(), end=" ")
# TODO: manipulate items from either end
d.popleft()
d.pop()
print(d)
d.append(1)
d.appendleft(2)
print(d)
# TODO: use an index to get a particular item
print(d[-1])
print(d[0])