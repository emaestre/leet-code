class Solution:
    def singleNumber(self, nums):
        count_map = {}

        for num in nums:
            if(num in count_map):
                count_map[num] += 1
            else:
                count_map[num] = 1

        for key in count_map:
            if(count_map[key] == 1):
                return key
