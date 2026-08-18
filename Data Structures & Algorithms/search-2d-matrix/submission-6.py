class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        left = 0
        right = r * c -1

        while left <= right:
            mid = (left + right)//2
            row, col = mid // c, mid % c
            value = matrix[row][col]

            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        return False