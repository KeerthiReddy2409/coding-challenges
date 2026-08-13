class Solution:
    def matchPlayersAndTrainers(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        l,r=0,0
        while l<m and r<n:
            if s[l]>=g[r]:
                r+=1
            l+=1
        return r