from collections import defaultdict

class Solution:
    def findMaxLength(self, nums) -> int:
        dir = {}
        dir[0] = -1
        maxlen = 0
        count = 0
        numsLen = len(nums)
        
        for i in range(numsLen):
            count = count + (1 if nums[i] == 1 else -1)
            if (count in dir):
                maxlen = max(maxlen, i - dir[count])
            else:
                dir[count] = i
            
        return maxlen
