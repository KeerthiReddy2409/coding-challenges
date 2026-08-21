class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        global ans
        ans=0
        def f(i,x):
            global ans
            if i==n:
                ans+=x
                return 
            f(i+1,x)
            f(i+1,x^nums[i])
        f(0,0)
        return ans
                