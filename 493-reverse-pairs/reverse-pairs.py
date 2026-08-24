class Solution:
    def reversePairs(self, arr: List[int]) -> int:

        def merge(l, mid, r):
            count = 0

            j = mid + 1

            for i in range(l, mid + 1):
                while j <= r and arr[i] > 2 * arr[j]:
                    j += 1

                count += j - (mid + 1)

            temp = []
            i = l
            j = mid + 1

            while i <= mid and j <= r:

                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= r:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[l + k] = temp[k]

            return count

        def merge_sort(l, r):
            if l >= r:
                return 0

            mid = (l + r) // 2

            count = merge_sort(l, mid)
            count += merge_sort(mid + 1, r)
            count += merge(l, mid, r)

            return count

        return merge_sort(0, len(arr) - 1)