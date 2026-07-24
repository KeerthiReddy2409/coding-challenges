class Solution:
    def countEven(self, num: int) -> int:
        x=sum(int(i) for i in str(num))
        if x % 2 == 0:
            return num // 2
        return (num - 1) // 2