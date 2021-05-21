arr = []
arr.append(x)           # append to the end of the list
arr.insert(index, x)
arr.pop()               # pop from end
arr.pop(0)              # pop from front

while contion:          # No () 

if not tmp              # check null

# dictionary
map = dict()
for key in map.keys():
val = map[key] or map.get(key)
del map[key]            # delete the entry with key
dict[c] = dict.get(c, 0) + 1
for key,value in dict.items():

# for range
for i in range(n)
for i in range(2,8)
for i in range(n-1, -1, -1)

# init array with values:
arr = [0]*n or arr = [0 for i in range(n)]

# sort
sorted()                # apply to any iterable item !!! will return a list of sorted elements
list.sort()             # only list can use .sort(), good to use for 2d array: sort based on arr[0]
arr.sort(key = lambda x: (x[0], -x[1]))  # first element 从小到大， second element 从大到小

# get a sorted string: sort string to charaters -> then join
s = "".join(sorted(s))

# list
arr[::-1]                               # reverse list
arr[-1] == arr[len(arr)-1]              # last element of list

# min heap / priority queue
heap = []
heapq.heappush(heap, item)          # push item into heap
heapq.heappop(heap)                 # pop and return the smallest item from heap
heapq.heapify(arr)                  # Transform list arr into a min heap
heapq.pushpop(heap, iteam)
heapq.heapreplace(heap, iteam)      # poppush

# For max heap: everything with "-" sign
heapq.heappush(heap, -value)
-heapq.heappop(heap)

float('-inf')
-sys.maxsize

# string to list
slist = list(s)

# list to string
''.join(slist)

# 判断 char isDigit
c.isdigit()

versions1 = [int(v) for v in version1.split(".")]

Note:
In binary search
while start < end:
    sth = mid+1
    sth_else = mid 
OR 
while start <= end:
    sth = mid+1
    sth_else = mid-1