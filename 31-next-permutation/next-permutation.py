class Solution:
    def nextPermutation(self, n: List[int]) -> None:

        x=len(n)-1
        for i in range(len(n)-2,-1,-1):
            if (n[i])<(n[i+1]):
                x=i
                break
        if x==len(n)-1:
            t=len(n)
            for i in range(t//2):
                n[i],n[t-i-1]=n[t-i-1],n[i]
        else:
            y = len(n)-1
            while (n[y]) <= (n[x]):
                y -= 1
            n[x],n[y]=n[y],n[x]
            n[x+1:]=reversed(n[x+1:])

 