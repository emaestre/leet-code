class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        current = 0
        nums_len = len(nums)
        
        while current < nums_len:
            if (nums[current] != 0):
                nums[current], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[current]
                lastNonZeroFoundAt += 1
            
            current += 1