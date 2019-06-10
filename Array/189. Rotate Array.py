# Solution based on Reversal Algorithm (Right rotate):
#  n = len(ar)
#  k = k%n
#  Assume ar is divided in place into 2 parts A,B
# 1. A [0..n-k-1] B[n-k..n-1]
# 2. reverse A to get ArB
# 3. reverse B to get ArBr
# 4. reverse all to get the k step rotation array.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - k - 1)
        # print('1st reverse', nums)
        self.reverse(nums, n - k, n - 1)
        # print('2nd reverse', nums)
        self.reverse(nums, 0, n - 1)

    def reverse(self, a, start, end):
        while start < end:
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
            start += 1
            end -= 1
