class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        new=[]
        for row in grid:
            for col in row:
                new.append(col)
        k=k%len(new)
        left=0
        right=len(new)-1
        while left<right:
            new[left],new[right]=new[right],new[left]
            left+=1
            right-=1
        left=0
        right=k-1
        while left<right:
            new[left],new[right]=new[right],new[left]
            left+=1
            right-=1
        left=k
        right=len(new)-1
        while left<right:
            new[left],new[right]=new[right],new[left]
            left+=1
            right-=1
        row=len(grid)
        col=len(grid[0])
        out=[[] for _ in range(row)]
        num=0
        for i in range(row):
            for j in range(col):
                out[i].append(new[num])
                num+=1
        return out
        