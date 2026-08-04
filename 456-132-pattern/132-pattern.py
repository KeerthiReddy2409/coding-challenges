class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float('-inf')
        s = []
        for i in nums[::-1]:    
            if i < third:
                return True
            while s and i > s[-1]:
                third = s.pop()
            s.append(i)
        return False