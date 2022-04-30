import collections
from curses import curs_set
from typing import List


# 1. Haiku

# def haiku(words, syllables):
#     left, pos = 0, 0
#     targets, i = [5, 7, 5], 0
#     result = []
#     while left < len(words):
#         currWord = words[pos]
#         numSyllables = syllables[currWord]
#         if numSyllables < targets[i]:
#             targets[i] -= numSyllables
#             pos += 1
#         elif numSyllables == targets[i]:
#             i += 1
#             result.append(' '.join(words[left, pos+1]))
#             pos += 1
#             if i == 3:
#                 return result
#         else:
#             left += 1
#             result = []
#             pos = left
#             targets, i = [5, 7, 5], 0
#     return []


''' 
2. Schedules (和 lc 370 很像)
Input: A list of [start, end] representing orders received in a car rental shop.
Output: the minimum number of cars required to fulfill the requests.
'''


def carRental(orders):
    endTime = max(orders, key=lambda x: x[1])[1]
    rentals = [0]*(endTime+2)
    for order in orders:
        rentals[order[0]] += 1
        rentals[order[1]+1] -= 1
    for i in range(1, endTime+2):
        rentals[i] += rentals[i-1]
    return max(rentals)
# print(carRental([[0, 3], [1, 4], [2, 5]]))


'''
lc 79 Word Search
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.bfs(i, j, board, word) == True:
                    return True
        return False

    def bfs(self, i, j, board, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        board[i][j] = '.'
        flag = self.bfs(i+1, j, board, word[1:]) or self.bfs(i-1, j, board, word[1:]) or self.bfs(
            i, j+1, board, word[1:]) or self.bfs(i, j-1, board, word[1:])
        board[i][j] = word[0]
        return flag


''' 
lc 772
Basic Calculator III
'''


class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, num = [], '+', 0
        for i, c in enumerate(s + '+'):
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            elif c in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                if c == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = c, 0
        return sum(stack)


'''
lc 1376 Employee
'''


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = collections.defaultdict(list)
        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)
        return self.dfs(headID, children, informTime)

    def dfs(self, head, children, informTime):
        if head not in children:
            return 0
        maxTime = 0
        for child in children[head]:
            time = self.dfs(child, children, informTime)
            maxTime = max(maxTime, time)
        return maxTime+informTime[head]


''' 
lc 273. Integer to English Words
'''


class Solution:
    def __init__(self):
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty",
                     "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        thousands_idx = 0
        res = ""
        while num > 0:
            if num % 1000 != 0:
                words = self.getWords(num % 1000)
                res = words + self.THOUSANDS[thousands_idx] + ' ' + res
            num //= 1000
            thousands_idx += 1
        return res.strip()

    def getWords(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.LESS_THAN_20[num] + ' '
        elif num < 100:
            return self.TENS[num//10] + ' ' + self.getWords(num % 10)
        else:
            return self.LESS_THAN_20[num//100] + " Hundred " + self.getWords(num % 100)


'''
lc 269 Alien Dictionary (这题似乎已经不出了, good for practice of topological search)
'''


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        map = collections.defaultdict(set)
        degree = collections.defaultdict(int)

        for word in words:
            for l in word:
                degree[l] = 0

        for i in range(len(words)-1):
            currWord = words[i]
            nextWord = words[i+1]
            length = min(len(currWord), len(nextWord))
            for j in range(length):
                if currWord[j] != nextWord[j]:
                    if nextWord[j] not in map[currWord[j]]:
                        map[currWord[j]].add(nextWord[j])
                        degree[nextWord[j]] += 1
                    break
                elif j == length-1 and len(currWord) > len(nextWord):
                    return ""

        queue = []
        for key in degree.keys():
            val = degree[key]
            if val == 0:
                queue.append(key)

        result = ""
        while queue:
            letter = queue.pop(0)
            for neighbour in map[letter]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    queue.append(neighbour)
            result += letter
        if len(result) != len(map):
            return ""
        return result


'''
lc 588. File System
'''


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.content = ""


class FileSystem:

    def __init__(self):
        self.root = Node()

    def getNode(self, path, create):
        if path == '/':
            return self.root
        curr = self.root
        for directory in path[1:].split('/'):
            if not curr.children.get(directory) and create == False:
                return None
            # curr.children[directory] = Node()
            curr = curr.children[directory]
        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.getNode(path, False)
        if not curr:
            return []
        if curr.content:  # file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:

        self.getNode(path, True)
        return

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.getNode(filePath, True)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.getNode(filePath, False)
        return node.content


'''
lc 68. Text Justification
'''


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n_letter, n_word, curr = 0, 0, []
        lines = []
        for word in words:
            if n_letter + n_word + len(word) > maxWidth:
                if len(curr) == 1:
                    lines.append(curr[0]+' '*(maxWidth-n_letter))

                else:
                    n_space, mod = divmod(maxWidth - n_letter, n_word-1)
                    for i in range(mod):
                        curr[i] += ' '
                    lines.append((' '*n_space).join(curr))
                    # currLine = ""
                    # for i,w in enumerate(curr):
                    #     currLine += w
                    #     if i == len(curr)-1:
                    #         break
                    #     currLine += ' '*n_space
                    #     if mod > 0:
                    #         currLine += ' '
                    #         mod -= 1
                    # lines.append(currLine)
                n_letter = len(word)
                n_word = 1
                curr = [word]
            else:
                n_letter += len(word)
                n_word += 1
                curr.append(word)
        lines.append(' '.join(curr) + ' '*(maxWidth - len(curr)-n_letter+1))
        return lines


'''
lc 23. Merge k sorted List
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        dummy = ListNode(0)
        curr = dummy
        count = 0
        for node in lists:
            if node:
                count += 1
                heapq.heappush(pq, (node.val, count, node))
        while len(pq) > 0:
            currMin = heapq.heappop(pq)
            curr.next = currMin[2]
            curr = curr.next
            if curr.next:
                count += 1
                heapq.heappush(pq, (curr.next.val, count, curr.next))
        return dummy.next


''' 
CSV parser
'''


def parse(lines):
    result = []
    currStr = ""
    isQuoted = False
    i = 0
    while i < len(lines):
        c = lines[i]
        if isQuoted == False:
            if c == '"':
                isQuoted = True
            elif c == ',':
                result.append(currStr)
                currStr = ""
            else:
                currStr += c
        else:
            if c == '"':
                if i < len(lines)-1 and lines[i+1] == '"':
                    currStr += '"'
                    i += 1
                else:
                    isQuoted = False
            else:
                currStr += c
        i += 1

    if currStr != "":
        result.append(currStr)
    return "|".join(result)


test = 'Alexandra Alex,"Alexandra Alex,","Alexandra ""Alex""","""Alexandra Alex""","Alexandra ""Alex""","""Alexandra ""Alex"""""'
test1 = "John,Smith,john.smith@gmail.com,Los Angeles,1"
test2 = "\"Alexandra \"\"Alex\"\"\",Menendez,alex.menendez@gmail.com,Miami,1"

print(parse(test))
print(parse(test1))
print(parse(test2))
