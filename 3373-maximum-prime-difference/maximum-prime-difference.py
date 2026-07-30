class Solution:
    x=[1]*101
    x[0]=0
    x[1]=0
    n=int(100**0.5)
    for i in range(2,n+1):
        if x[i]==1:
            for j in range(i*i,101,i):
                x[j]=0
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while self.x[nums[l]]==0 and l<n:
            l+=1
        while self.x[nums[r]]==0 and r>-1:
            r-=1
        # print(l,r)
        return (r-l)


