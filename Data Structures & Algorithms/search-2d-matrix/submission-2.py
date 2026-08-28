"""
first problem, find the sub array that contains the target
we can likely use binary search for this

left = 0
right = len(matrix) - 1
target_row_idx = -1

while left <= right:
    mid = (left + right) // 2
    if matrix[mid][0] > target:
        right = mid - 1
    elif matrix[mid][-1] < target:
        left = mid + 1
    else:
        target_row_idx = mid
        break

if target_row_idx == -1:
    return False

row = matrix[target_row_idx]
left = 0
right = len(row) -1

while left <= right:
    mid = (left + right) // 2
    if row[mid] > target:
        right = mid -1
    elif row[mid] < target:
        left = mid + 1
    else:
        return True
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        target_row_idx = -1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                target_row_idx = mid
                break

        if target_row_idx == -1:
            return False

        row = matrix[target_row_idx]
        left = 0
        right = len(row) -1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] > target:
                right = mid -1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False
        