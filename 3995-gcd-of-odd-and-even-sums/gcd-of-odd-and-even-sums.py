class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        #test
        e=0
        o=0
        for i in range(1,2*n+1):
            if i%2==0:
                e+=i
            else:
                o+=i
        # print(e,o)
        while o!=0:
            e,o=o,e%o
        return e