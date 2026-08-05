class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(cap):
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k

        l, r = min(nums), max(nums)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans