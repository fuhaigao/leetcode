class Solution:
    '''
    熟练掌握 sort by setting key=func() 就可以秒杀
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key = self.sort)
    def sort(self,logs):
            a,b = logs.split(' ', 1)
            if b[0].isalpha():
                return (0,b,a)
            else:
                return (1,None,None)