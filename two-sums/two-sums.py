class Solution:
    def twoSum(self, nums, target):
        nums_len = len(nums)
        hash_map = {}
        result = []
        
        for index in range(nums_len):
            difference = target - nums[index]
            if(difference in hash_map):
                result.append(index)
                result.append(hash_map[difference])
                return result
            
            hash_map[nums[index]] = index
        
        return result