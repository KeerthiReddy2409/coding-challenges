class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[d/s for d,s in zip(dist, speed)]
        t=0
        m=0
        time.sort()
        for i in time:
            if i<=t:
                return m
            else:
                t+=1
                m+=1
        return m
        