class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        matrix = [[0]*numCourses for i in range(numCourses)]
        indegree = [0]*numCourses
        for entry in prerequisites:
            ready = entry[0]
            pre = entry[1]
            matrix[pre][ready] = 1
            indegree[ready] += 1
        
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        index = 0
        while queue:
            course = queue.pop(0)
            res.append(course)
            index += 1
            for i in range(numCourses):
                if matrix[course][i] == 1:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)
        return res if index == numCourses else []