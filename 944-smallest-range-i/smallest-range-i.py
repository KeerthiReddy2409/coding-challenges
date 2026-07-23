class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a=min(nums)
        b=max(nums)
        x=(a+b)//2
        return max(b-k,x)-min(a+k,x)
