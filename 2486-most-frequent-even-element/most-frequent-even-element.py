class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        nums.sort()
        d=Counter(nums)
        ans=-1
        f=0
        for i in d.keys():
            if i%2==0:
                if d[i]>f:
                    ans=i
                    f=d[i]
        return ans
