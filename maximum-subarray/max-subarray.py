class Solution:
    def maxSubArray(self, nums) -> int:
        current = 0
        max_sum = -2147483647
        
        if(len(nums) == 1):
            return nums[0]
        
        for num in nums:
            current = max(num, current + num)
            max_sum = max(current, max_sum)
        
        return max_sum