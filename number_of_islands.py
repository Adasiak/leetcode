from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # print("kysywdgye")
        land = 0
        for i in range(len(grid)):
            index1 = i - 1 if i > 0 else 0
            for j in range(len(grid[i])):
                index2 = j - 1 if j > 0 else 0
                
                if i == 0:
                    if j == 0:
                        if grid[i][j] == "1":
                            land += 1
                    else:
                        if grid[i][j] == "1" and grid[i][index2] == "0":
                            land += 1
                
                
                # and index2 == 0 and grid[i][j] == "1":
                #     land += 1
                # elif grid[i][j] == "1" and grid[i][j] == "0" and grid[i][j] == "0":
                #     land += 1 
                
                pass
                
                
        
        
        # pass
        return land






grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
mm = Solution()
result = mm.numIslands(grid)
expected = 1
if result != expected:
    raise ValueError