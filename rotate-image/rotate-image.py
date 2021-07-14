class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(mat),len(mat[0])
        for i in range(m):
            for j in range(i,m):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for i in range(m):
            for j in range(m//2):
                mat[i][j],mat[i][-j-1] =mat[i][-j-1],mat[i][j]
        return mat