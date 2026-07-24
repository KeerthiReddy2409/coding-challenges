class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            x=i
            c=[]
            while x>0:
                c.append(x%10)
                x=x//10
            ans+=c[::-1]
            c=[]
        return ans
