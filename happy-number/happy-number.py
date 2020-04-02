class Solution:
    def getSumOfSquareDigits(self, n: int) -> int:
        res = 0
        for digit in str(n):
            digit = int(digit)
            res += digit*digit
        
        return res
    
    def isHappy(self, n: int) -> bool:
        if(n == 1 or n == 7):
            return True
        
        if(n < 10):
            return False
        
        return self.isHappy(self.getSumOfSquareDigits(n))