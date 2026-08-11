class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if k == 0:
            return n

        x = nums[n-k]
        l, h = 0, n

        while l < h:
            m = (l+h)//2
            if nums[m] < x:
                l = m+1
            else:
                h = m

        return l