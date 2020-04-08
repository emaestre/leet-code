class Solution:
    def countElements(self, arr) -> int:
        count = 0
        
        for number in arr:
            if(number + 1 in arr):
                count += 1
        
        return count