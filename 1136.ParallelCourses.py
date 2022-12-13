class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        requisites = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for i in range(1,n+1):
            degrees[i] = 0
        
        for relation in relations:
            degrees[relation[1]] += 1
            requisites[relation[0]].append(relation[1])
        
        queue = collections.deque()
        for course in degrees:
            if degrees[course] == 0:
                queue.append(course)
        
        semesters = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                n -= 1
                for nextCourse in requisites[course]:
                    degrees[nextCourse] -= 1
                    if degrees[nextCourse] == 0:
                        queue.append(nextCourse)
        return semesters if n == 0 else -1