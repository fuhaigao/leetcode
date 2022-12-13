class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requisites = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for course in range(numCourses):
            indegree[course] = 0
        for entry in prerequisites:
            indegree[entry[0]] += 1
            requisites[entry[1]].append(entry[0])
        queue = collections.deque()
        for course in indegree:
            if indegree[course] == 0:
                queue.append(course)
        count = 0
        while queue:
            course = queue.popleft()
            for course in requisites[course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            count += 1
        return True if count == numCourses else False