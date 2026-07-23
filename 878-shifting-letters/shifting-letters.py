class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans=""
        sum=0
        for i in range(len(s)-1,-1,-1):
            sum+=shifts[i]
            ans+=(chr((ord(s[i]) - ord('a') + sum) % 26 + ord('a')))
        return ans[::-1]
            