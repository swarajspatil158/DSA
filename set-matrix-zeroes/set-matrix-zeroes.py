class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(mat),len(mat[0])
        row,col = set(),set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    row.add(i)
                    col.add(j)
                    
        for i in row:
            for j in range(n):
                mat[i][j]=0
                
        for i in col:
            for j in range(m):
                mat[j][i]=0
        return mat
                
        
                    