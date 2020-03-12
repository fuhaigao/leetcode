class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pt={}
        st={}
        str=str.split()
        if len(pattern)!=len(str):return False
        for i in range(len(pattern)):
            if pt.get(pattern[i],0)!=st.get(str[i],0):return False
            pt[pattern[i]]=i+1
            st[str[i]]=i+1
        return True
