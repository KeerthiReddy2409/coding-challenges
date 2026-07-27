class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def f(i,j):
            if i < 0:
                return sum(ord(c) for c in s2[:j+1])
            if j < 0:
                return sum(ord(c) for c in s1[:i+1])
            if s1[i]==s2[j]:
                return f(i-1,j-1)
            return min(ord(s1[i])+f(i-1,j),ord(s2[j])+f(i,j-1))
        return f(len(s1)-1,len(s2)-1)
            