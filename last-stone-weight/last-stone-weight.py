class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort(reverse=True)
        stonesLen = len(stones)
        
        if(stonesLen == 0):
          return 0
        
        if(stonesLen == 1):
          return stones[0]
        
        firstStone = stones[0]
        secondStone = stones[1]
        stones.remove(firstStone)
        stones.remove(secondStone)
          
        if(not firstStone == secondStone):
          newStone = firstStone - secondStone
          stones.append(newStone)
        
        return self.lastStoneWeight(stones)