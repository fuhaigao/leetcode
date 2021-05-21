class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        count = 0
        while queue:
            course = queue.pop(0)
            for i in range(numCourses):
                if matrix[course][i] == 1:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)
            count += 1
        return True if count == numCourses else False