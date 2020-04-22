# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def searchIndex(self, index, pointer, rows, cols, binaryMatrix):
        if pointer['x'] < 0 or pointer['x'] >= rows or pointer['y'] < 0 or pointer['y'] >= cols:
            return

        i = binaryMatrix.get(pointer['x'], pointer['y'])
        if i == 1:
            index.append(pointer['y'])
            pointer['y'] -= 1
        else:
            pointer['x'] += 1
        
        self.searchIndex(index, pointer, rows, cols, binaryMatrix)
        
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        pointer = {
            'x': 0,
            'y': cols - 1
        }
        index = []
        index.append(-1)
        self.searchIndex(index, pointer, rows, cols, binaryMatrix)
        return index.pop()