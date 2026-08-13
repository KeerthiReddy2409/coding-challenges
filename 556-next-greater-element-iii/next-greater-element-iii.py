class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=list(str(n))
        x=len(n)-1
        for i in range(len(n)-2,-1,-1):
            if int(n[i])<int(n[i+1]):
                x=i
                break
        if x==len(n)-1:
            return -1
        y = len(n)-1
        while int(n[y]) <= int(n[x]):
            y -= 1
        n[x],n[y]=n[y],n[x]
        n[x+1:]=reversed(n[x+1:])
        ans=int("".join(n))
        return ans if ans<2**31 else -1
 