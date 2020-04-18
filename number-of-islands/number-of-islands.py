class Solution:
    def markVisitedIsland(self, grid, i: int, j: int, rows: int, columns: int) -> None:
        # Checking the boundaries
        if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != '1':
            return
        
        # Marking the cell as visited
        grid[i][j] = 'v'
        
        # We traverse the cells in the 4 possible directions to mark other islands
        self.markVisitedIsland(grid, i + 1, j, rows, columns)
        self.markVisitedIsland(grid, i, j + 1, rows, columns)
        self.markVisitedIsland(grid, i - 1, j, rows, columns)
        self.markVisitedIsland(grid, i, j - 1, rows, columns)
        
    
    def numIslands(self, grid) -> int:
        # counter for num of islands
        num_of_islands = 0
        # num of rows
        rows = len(grid)
        # if we don't have rows, we return 0
        if(rows == 0):
            return 0
        
        # num of columns
        columns = len(grid[0])
        
        for i in range(rows):
            for j in range(columns):
                # When found a piece of land, we visit the adyacent cells with a DFS
                if grid[i][j] == '1':
                    self.markVisitedIsland(grid, i, j, rows, columns)
                    num_of_islands += 1
        
        return num_of_islands