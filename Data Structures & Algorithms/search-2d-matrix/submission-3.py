class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == target:
                    return True

        return False