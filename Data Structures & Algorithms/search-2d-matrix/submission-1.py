"""
l = 0
r = len(arr) - 1
mid = 0

while l <= r:
    mid = (l + r) // 2
    if arr[mid][-1] > target: 
        r = mid - 1
    elif arr[mid][0] < target :
        l = mid + 1
    else:
        return mid



step - 0
l    - 0
r    - 2
mid  - 0

step - 1
l    - 0
r    - 2
mid  - 1


"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(matrix):
            l = 0
            r = len(matrix) - 1
            mid = 0

            while l <= r:
                mid = (l + r) // 2
                if matrix[mid][0] > target and matrix[mid][-1] > target:
                    r = mid - 1
                elif matrix[mid][0] < target and matrix[mid][-1] < target:
                    l = mid + 1
                else:
                    return mid

            return -1
        row = find_row(matrix)

        if row == -1:
            return False

        l = 0
        r = len(matrix[row]) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
                
        