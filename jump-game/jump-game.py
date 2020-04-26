class Solution:
    def canJump(self, nums) -> bool:
        nums_len = len(nums)
        last_pos = nums_len - 1
        for i in range(nums_len - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
        