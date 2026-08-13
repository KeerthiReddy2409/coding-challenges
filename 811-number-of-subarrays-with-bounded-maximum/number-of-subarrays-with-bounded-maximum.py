class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def c(x):
            ans=0
            l=0
            for i in nums:
                if i<=x:
                    l+=1
                    ans+=l
                else:
                    l=0
            return ans
        return c(right)-c(left-1)