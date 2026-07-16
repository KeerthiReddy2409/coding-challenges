class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return sum([str(i).count(str(digit)) for i in nums])