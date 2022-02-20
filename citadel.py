import collections
import math

# 1. Prime Factor Visitation
class PFVSolution: 
    def __init__(self):
        self.states = []

    def update_states(self, n):
        for i in range(n-1, len(self.states), n):
            self.states[i] ^= 1

    def prime_factor_visitation(self, states, numbers):
        self.states = states
        primes = collections.Counter()
        for num in numbers:
            # Find unique prime factors and update counter
            i = 2
            while i*i <= num:
                if num%i == 0:
                    primes[i] += 1
                while num%i == 0:
                    num //= i
                i += 1
            if num > 1:
                primes[num] += 1
        # If the prime exist an odd number of times, turn on/off the bulb
        for n in primes:
            if primes[n]%2:
                self.update_states(n)
        return self.states

test = PFVSolution()
print(test.prime_factor_visitation([1,1,0,0,1,1,0,1,1,1], [3,4,15]))

# 2. Disk Space Analysis
class DSASolution:

    def findMax(self, space, segement):
        result = 0
        queue = []
        for i in range(len(space)):
            if len(queue)>0 and queue[0] < i-segement+1:
                queue.pop(0)
            while len(queue)>0 and space[queue[-1]] >space[i]:
                queue.pop()
            queue.append(i)
            if i >= segement-1:
                result = max(result, space[queue[0]])
        return result


test1 = DSASolution()
# print(test1.findMax([8,2,4,6], 2))
print(test1.findMax([1,2,3,1,2], 2))

# 3. Do They Belong? (Triangle)
class TriangleSolution:
    def area(self, x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)
    
    def isTriangle(self, x1, y1, x2, y2, x3, y3):
        a = math.sqrt(pow(x2-x1, 2) + pow(y2-y1,2))
        b = math.sqrt(pow(x3-x1, 2) + pow(y3-y1,2))
        c = math.sqrt(pow(x3-x2, 2) + pow(y3-y2,2))
        if (a+b >c) and (a+c>b) and (b+c>a):
            return True
        return False

    def pointsBelongTo(self, x1, y1, x2, y2, x3, y3, p1, p2, q1, q2):
        if self.isTriangle(x1, y1, x2, y2, x3, y3) == False:
            return 0
        pFlag = False
        qFlag = False
        if self.area(x1, y1, x2, y2, p1, p2) + self.area(x1, y1, x3, y3, p1, p2) + self.area(x2, y2, x3, y3, p1, p2) == self.area(x1, y1, x2, y2, x3, y3):
            pFlag = True
        if self.area(x1, y1, x2, y2, q1, q2) + self.area(x1, y1, x3, y3, q1, q2) + self.area(x2, y2, x3, y3, q1, q2) == self.area(x1, y1, x2, y2, x3, y3):
            qFlag = True
        if pFlag and not qFlag:
            return 1
        if not pFlag and qFlag:
            return 2
        if pFlag and qFlag:
            return 3
        if not pFlag and not qFlag:
            return 4

test2 = TriangleSolution()
print(test2.pointsBelongTo(3,1,7,1,5,5,5,2,6,3))

# 4. Global maximum
class LMSolution:
    def isExist(self, A, B, mid):
        count = 1
        prev = A[0]
        for i in range(1, len(A)):
            if A[i] - prev >= mid:
                prev = A[i]
                count += 1

                if count == B:
                    return True
        return False

    def find_min_difference(self, A, B):
        # Sort the list for binary search
        A.sort()
        # Binary Search find the maximum difference\
        start, end = 0, A[-1]-A[0]
        ans = 0

        while start <= end:
            mid = (start+end)//2
            if self.isExist(A, B, mid):
                # update ans to current maximum
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans


test3 = LMSolution()
print("Find min difference: ", test3.find_min_difference([1,2,3,5], 3))

# 5. Count Inversion
class CIClass:
    def getInvCount(self, nums):
        invCount = 0
        for i in range(1, len(nums)-1):
            small = 0
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    small += 1
            large = 0
            for j in range(i-1, -1, -1):
                if nums[j] > nums[i]:
                    large += 1
            invCount += large*small
        return invCount

test4 = CIClass()
print("Count Inversions: ", test4.getInvCount([8,4,2,1]))

# 6. Sprint Training
class STClass:
    def getMostVisited(self, n, sprints):
        counter = [0]*(n+1)
        for i in range(0, len(sprints)-1):
            start = min(sprints[i], sprints[i+1])
            end = max(sprints[i], sprints[i+1])
            counter[start] += 1
            counter[end+1] -= 1
        maxVisited = -1
        result = -1
        for i in range(1, n):
            counter[i] += counter[i-1]
            if counter[i] > maxVisited:
                maxVisited = counter[i]
                result = i
        return result

test5 = STClass()
print("Sprint Training Result: ", test5.getMostVisited(5,[2,4,1,3]))

# 7. Portfolio Balances
class PBClass:
    def getMaximumInvestment(self, n, rounds):
        investments = [0]*(n+1)
        for left, right, contribution in rounds:
            investments[left-1] += contribution
            investments[right] -= contribution
        res = -1
        for i in range(1, n+1):
            investments[i] += investments[i-1]
            res = max(res, investments[i])
        return res
test6 = PBClass()
print("Portfolio Balances: ", test6.getMaximumInvestment(5, [[1,2,10], [2,4,5], [3,5,12]]))

# 8. Maximum number of teams that can be formed with given persons
# Greedy: Always choose two people from group with more members
class TeamSolution:
    def maxTeam(self, n, m):
        count = 0
        while (self.isMemberEnough(n,m)):
            count += 1
            if n > m:
                n -= 2
                m -= 1
            else:
                n -= 1
                m -= 2
        return count
    
    def isMemberEnough(self, n, m):
        if (n>=2 and m>=1) or (n>=1 and m>=2):
            return True
        return False
test7 = TeamSolution()
print("Team Solution: ", test6.maxTeam(4,5))

# 9. Whole Minute Dilemma (LC 1010)
class WMDSolution:
    def numPairsDivisibleBy60(self, time) -> int:
        ans, cnt = 0, collections.Counter()
        for t in time:
            theOther = -t % 60
            ans += cnt[theOther]
            cnt[t % 60] += 1
        return ans

# 10. Triplets (LC 259)
class TriSolution:
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    # if (i,l,r) < target, then (i,l,r), (i,l,r-1),..., (i,l,l+1) will all < target, totally (r-l) triplets
                    count += r-l
                    l += 1
                else:
                    r -= 1
        return count


# 11. LC 829. Consecutive Numbers Sum
class CNSSolution:
    '''
    n = (x+x+m-1)*(m/2)
    calculate x based on m OR calculate m based on x
    eaiser for x based on m:
    x = n/m - m/2 + 1/2
    x = (2n-m*m+m)/(2m)
    At this point, m must smaller than sqrt(2n)
    '''
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        m = 1
        while m < sqrt(2*n):
        # for m in range(1, sqrt(2*n)):
            if (2*n-m*m+m) % (2*m) == 0 :
                count += 1
            m += 1
        return count

# 12. LC 370. Range Addition
class RASolution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        results = [0]*(length+1)
        for start, end, inc in updates:
            results[start] += inc
            results[end+1] -= inc
        
        for i in range(1, length+1):
            results[i] += results[i-1]
        return results[:length]

# 13. LC 241: Different ways to add parentheses
class ParenthesesSolution:
    def diffWaysToCompute(self, input: str):
        res = []
        if (input.isdigit()):
            return [int(input)]
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for num1 in left:
                    for num2 in right:
                        res.append(self.calculate(num1, num2, input[i]))
        return res
    def calculate(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        if op == "*":
            return num1 * num2

# 14. LC 1048: StringChain
class StringChainSolution:
    '''
    DP Question
    global maximum keep update the longest chain
    We need to check all words that shorter than current word (any shorter word is possibly a predecessor). Use a dictionary to keep track the chain for traversed word
    '''
    def longestStrChain(self, words):
        wordToChain = dict()
        words.sort(key=lambda x:len(x))
        result = 1
        for word in words:
            wordToChain[word] = 1
            for i in range(len(word)):
                possiblePrecessor = word[:i]+word[i+1:len(word)]
                if possiblePrecessor in wordToChain:
                    wordToChain[word] = wordToChain[possiblePrecessor]+1
                    result = max(result, wordToChain[word])
        return result
                