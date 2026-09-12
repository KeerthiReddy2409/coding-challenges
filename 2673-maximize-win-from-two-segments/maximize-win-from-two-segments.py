class Solution:
    def maximizeWin(self, prizePositions, k):
        n = len(prizePositions)
        if 2*(k+1)>max(prizePositions)-min(prizePositions):
            return len(prizePositions)

        best = [0] * n
        left = 0

        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1

            length = right - left + 1

            if right > 0:
                best[right] = best[right - 1]

            best[right] = max(best[right], length)

        ans = 0
        left = 0

        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1

            current = right - left + 1

            if left > 0:
                ans = max(ans, current + best[left - 1])

        return ans