class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        matrix.reverse()
        print(matrix)
        for r in range(N):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                print(matrix)
        """
        Do not return anything, modify matrix in-place instead.
        """
        