class Solution:
    def subarraySum(self, nums, k: int) -> int:
        dic = {
            0: 1
        }
        nums_len = len(nums)
        count = 0
        sub_sum = 0
        
        for i in range(nums_len):
            sub_sum += nums[i]
            if sub_sum - k in dic:
                count += dic[sub_sum - k]
            
            if sub_sum in dic:
                dic[sub_sum] += 1
            else:
                dic[sub_sum] = 1
        
        return count