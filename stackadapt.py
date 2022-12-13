# Given list of time intervals, find the index of the most overlapped time
# prefix sum
from termios import OFDEL


def mostOverlappedTime(intervals, n):
    times = [0]*(n+1)
    for start, end in intervals:
        times[start] += 1
        times[end+1] -= 1
    maxOverlaps, idx = 0, 0
    for i in range(n):
        times[i+1] += times[i]
        if times[i+1] > maxOverlaps:
            maxOverlaps = times[i+1]
            idx = i+1
    return idx

test1 = mostOverlappedTime([[0,1], [1,2], [0,2], [2,3]], 4)
print(test1)

# Given binary tree, 找最长路径 (lc543)
# dfs to find depth
class Solution:
    def __init__(self):
        self.maxLength = -1
    def findLongestPath(self, root):
        self.dfs(root)
        return self.maxLength
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # print(root.val, left, right)
        self.maxLength = max(self.maxLength, left+right+1)
        return max(left, right)+1

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

testRoot = TreeNode(1)
testRoot.left = TreeNode(2)
testRoot.right = TreeNode(3)
testRoot.right.left = TreeNode(4)
testRoot.right.left.left = TreeNode(5)
testRoot.right.right = TreeNode(6)

'''
    1
2      3
     4   6
    5
'''
sol = Solution()
print(sol.findLongestPath(testRoot))

# 潜水艇
# 一个潜艇在深度为n的水里，每次roll a dice（1-6）根据点数上浮对应的深度。给定n,k问你深度为n的潜艇k次浮上水面的概率是多少？ 如果深度不足r，上浮r会直接到水面
# dp (similar to 01 backpack)
def getNumberOfPossibleWays(n, k):
    largestPossibleNumber = k*6
    dp = [[0 for _ in range(largestPossibleNumber+1)] for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(1, k+1):
        for j in range(1, largestPossibleNumber+1):
            for val in range(1, min(7, j+1)):
                dp[i][j] += dp[i-1][j-val]
    return sum(dp[-1][n:])

depth = 7
throws = 2
numberOfPossibleWays = getNumberOfPossibleWays(depth, throws)
possibility = numberOfPossibleWays / pow(6,throws)
print(numberOfPossibleWays, possibility)

# 给你不停发牌（stream of items），你不知道什么时候结束，每张牌你可以选择fold or keep，你手上最多hold n 张. Find a strategy: 使得最后手上的牌是stream中的一个uniformly distributed randomized

# lc 1914

# lc 169 (Boyer-Moore Majority Vote Algorithm)

# lc 64


# Design restaurant

## Ordering Takeout

# We are building software for a restaurant which only allows customers to order takeout online. The restaurant has sent us their requirements below.

# ### Part 1

# First, we want to implement the menu system for the restaurant. 

# The restaurant primarily serves dishes, and wants to displays the dish's name & price to its customers:

# // ```
# // Dish
# //   - name
# //   - price
# // ```

# A list of dishes comprises a menu. At any given time of day the menu for the restaurant is restricted by what time of day it is (given in 24-hour format):
#    - 7-11 Breakfast Menu
#    - 12-15 Lunch Menu
#    - 16-21 Dinner Menu
#    - 7-21 All Day Menu


#  Given the above domain requirements, implement the following functions:
#    - `add_dish(dish)`: Adds a dish to it's given menu (either breakfast, lunch, dinner, or all day)
#    - `get_dishes(time)`: Returns the name & prices of the dishes available at a given time (given as an integer between 1-24). For example, if time is "12PM", this would return all the dishes available in both the lunch menu and all day menu.

# Part 2:
# support order features
# - add_order(dishes)
# - cancel_order(orderId)
# - get_oldest_order()

# Notes: 我面的时候第一部分写完觉得有些 implementation 并不是最合理的 （例如，get_dishes 会重复retrieve 同样的 dish 再去重，浪费了一些performance
# 面试官就让我口头说了 alternative solution 以及对应的trade off

import collections

class Dish:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Restaurant:
  def __init__(self):
    self.orderId = 0
    self.head = Order(-1, [])
    self.tail = Order(-2, [])
    self.head.next = self.tail
    self.tail.prev = self.head
    self.idToOrder = {}
    
    self.breakfast = []
    self.lunch = []
    self.dinner = []
    self.allDay = []
    self.time_mapping = collections.defaultdict(set)
    for i in range(7, 22):
      if 7 <= i <= 11:
        self.time_mapping[i].add("breakfast")
      if 12 <= i <= 15:
        self.time_mapping[i].add("lunch")
      if 16 <= i <= 21:
        self.time_mapping[i].add("dinner")
      if 7 <= i <= 21:
        self.time_mapping[i].add("allDay")
    self.menu_mapping = {
      "breakfast": self.breakfast,
      "lunch": self.lunch,
      "dinner": self.dinner,
      "allDay": self.allDay
    }
  
  def add_dish(self, dish, menu):
    if menu in self.menu_mapping:
      self.menu_mapping[menu].append(dish)
      return True
    return False
    
  def get_dishes(self, time):
    items = set()
    if time not in self.time_mapping:
      return None
    menu_names = self.time_mapping[time]
    for menu_name in menu_names:
      for dish in self.menu_mapping[menu_name]:
          items.add(dish)
    return list(items)
  
  def add_order(self, dishes):
    order = Order(self.orderId, dishes)
    self.idToOrder[self.orderId] = order
    self.orderId += 1
    headNext = self.head.next
    self.head.next = order
    order.next = headNext
    order.prev = self.head
    headNext.prev = order
    return self.orderId-1
    
    # HEAD <-> order <-> TAIL
  
  def cancel_order(self, orderId):
    order = self.idToOrder[orderId]
    order.prev.next = order.next
    order.next.prev = order.prev
  
  def get_oldest_order(self):
    oldest = self.tail.prev
    if oldest != self.head:
      self.cancel_order(oldest.id)
      return oldest
    return None
    

class Order:
  def __init__(self, orderId, dishes):
    self.id = orderId
    self.dishes = dishes
    self.prev = None
    self.next = None
  
    

restaurant = Restaurant()
dish = Dish("egg", 2)
restaurant.add_dish(dish, "breakfast")
dish2 = Dish("soda", 1)
restaurant.add_dish(dish2, "allDay")

dish3 = Dish("pizza", 4)
restaurant.add_dish(dish3, "dinner")
dish4 = Dish("sandwich", 3)
restaurant.add_dish(dish4, "lunch")

dishes = restaurant.get_dishes(23)
if dishes:
  for dish in dishes:
    print(dish.name, dish.price)
else:
  print("No dish")

dishes = [dish, dish2, dish3]
id1 = restaurant.add_order(dishes)
restaurant.add_order([dish2])
# restaurant.cancel_order(id1)
order1 = restaurant.get_oldest_order()
print("order1")
for dish in order1.dishes:
  print(dish)
  
print("order2")
for dish in restaurant.get_oldest_order().dishes:
  print(dish)