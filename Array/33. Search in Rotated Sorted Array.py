class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pivot = -1
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                pivot = i
                break

        # print(pivot)

        if pivot == -1:
            res = self.binary_search(nums, 0, n - 1, target)
        elif target >= nums[0]:
            res = self.binary_search(nums, 0, pivot, target)

        else:
            res = self.binary_search(nums, pivot + 1, n - 1, target)
            # print(nums[pivot+1:n])

        return res

    def binary_search(self, a, low, high, target):
        mid = (low + high) // 2
        # print(a[mid])
        while low <= high:
            if a[mid] == target:
                return mid
            elif a[mid] < target:
                low = mid + 1
            elif a[mid] > target:
                high = mid - 1
            mid = (low + high) // 2
        return -1
