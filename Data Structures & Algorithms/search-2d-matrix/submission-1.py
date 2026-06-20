class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1

        while bottom <= top:
            middle = (bottom + top) // 2

            if target < matrix[middle][0]:
                top = middle - 1
            
            elif target > matrix[middle][-1]:
                bottom = middle + 1
            
            else:
                l = 0
                r = len(matrix[middle]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if target > matrix[middle][m]:
                        l = m + 1

                    elif target < matrix[middle][m]:
                        r = m - 1
                    
                    else:
                        return True
                        
                return False
        
        return False