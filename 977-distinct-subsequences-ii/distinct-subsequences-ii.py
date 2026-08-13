class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=[0]*26
        t=0
        for c in s:
            i=ord(c)-ord('a')
            dp[i]=t+1
            t=sum(dp)%(10**9+7)
        return t