class Solution:
    def stringShift(self, s: str, shift) -> str:
        rotate = 0
        shiftLen = len(shift)
        for i in range(shiftLen):
            direction = shift[i][0]
            amount = shift[i][1]
            if(direction):
                rotate += amount
            else:
                rotate -= amount
        
        rotations = rotate % len(s)
        if(rotations > 0):
            res = s[-rotations:] + s[:-rotations]
        elif(rotations < 0):
            res = s[rotations:] + s[:rotations]
        else:
            res = s
            
        return res