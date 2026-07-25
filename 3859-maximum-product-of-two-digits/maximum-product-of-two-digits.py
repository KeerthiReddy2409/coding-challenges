class Solution:
    def maxProduct(self, n: int) -> int:
        m1=0
        m2=0
        while n>0:
            x=n%10
            if x>m1:
                m2=m1
                m1=x
            elif x>m2:
                m2=x
            n//=10
        return m1*m2