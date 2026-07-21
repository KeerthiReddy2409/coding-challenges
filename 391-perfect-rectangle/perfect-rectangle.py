class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area=0
        minx=miny=float('inf')
        maxx=maxy=float('-inf')
        s=set()
        for a,b,c,d in rectangles:
            area+=(c-a)*(d-b)
            minx=min(minx,a)
            miny=min(miny,b)
            maxx=max(maxx,c)
            maxy=max(maxy,d)
            for p in [(a,b),(a,d),(c,b),(c,d)]:
                if p in s:
                    s.remove(p)
                else:
                    s.add(p)
        if area!=(maxx-minx)*(maxy-miny):
            return False
        return s=={(minx,miny),(minx,maxy),(maxx,miny),(maxx,maxy)}