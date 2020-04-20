class Solution:
    def search(self, nums, target: int) -> int:
        return -1 if not target in nums else nums.index(target)
        