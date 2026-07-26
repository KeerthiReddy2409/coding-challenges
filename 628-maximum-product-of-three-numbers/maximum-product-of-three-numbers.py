class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        m1=m2=m3=float("-inf")
        u1=u2=float("inf")
        for i in nums:
            if i >m1:
                m3=m2
                m2=m1
                m1=i
            elif i>m2:
                m3=m2
                m2=i
            elif i>m3:
                m3=i
            if i<u1:
                u2=u1
                u1=i
            elif i<u2:
                u2=i
        return max(m1*m2*m3, m1*u1*u2)