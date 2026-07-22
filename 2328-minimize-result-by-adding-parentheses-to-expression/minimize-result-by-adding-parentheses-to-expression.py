class Solution:
    def minimizeResult(self, e: str) -> str:
        n=len(e)
        plus=-1
        for i in range(n):
            if e[i]=="+":
                plus=i
                break
        # print(plus)
        ans=float("inf")
        x,y=-1,-1
        for i in range(plus):
            for j in range(plus+1,n):
                if e[:i]!="":
                    a=int(e[:i])
                else:
                    a=1
                b=int(e[i:plus])+int(e[plus+1:j+1])
                if e[j+1:] != "":
                    c = int(e[j+1:])
                else:
                    c = 1
                if a*b*c<ans:
                    ans=a*b*c
                    x=i
                    y=j
        return e[:x]+'('+e[x:y+1]+')'+e[y+1:]
                
