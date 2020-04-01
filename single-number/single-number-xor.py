class Solution:
    def singleNumber(self, nums):
        current = 0
        for num in nums:
            current ^= num

        return current
