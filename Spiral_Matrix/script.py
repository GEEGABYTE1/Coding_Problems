class Solution:
    
    def spiralOrder(self, matrix):
        result = []
        col_checker = 0 
        for i in matrix:
            if len(i) == 1:
                col_checker += 1
    

        if len(matrix) == 0:
            return None
        
        elif len(matrix) == 1:                  # Only row 
            result = matrix[0]
            return result 

        elif col_checker == len(matrix):        # Only Cols
            for row in matrix:
                result.append(row[0])
            
            return result

        else:    
            row = 0 
            col = 0 
            temp_col = -2
            temp_row = -2
            
            row_counter = len(matrix[0])
            col_counter = len(matrix)
            
            for i in range(row_counter):
                current_num = matrix[row][col]
                result.append(current_num)
                col += 1
            
            col = 0 
            
            for i in range(col_counter - 1):
                current_num = matrix[row + 1][-1]
                result.append(current_num)
                row += 1
            
            row = 0
            
            for i in range(row_counter - 1):
                current_row = matrix[-1]
                current_num = matrix[-1][temp_col]
                result.append(current_num)
                temp_col -= 1

            if col_counter % 2 != 0:
                mid_row = len(matrix) // 2
            
                for i in range(col_counter - 2):
                    current_num = matrix[temp_row][0]
                    result.append(current_num)
                    temp_row -=  1
                
                
                for i in range(row_counter - 2):
                    current_num = matrix[mid_row][col + 1]
                    result.append(current_num)
                    col += 1
            else:
                
                return result


            
            
            return result

            



        




solution = Solution()


test_matrix = [[1,2, 3], [4, 5, 6], [7, 8, 9]]
test_matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
test_matrix3 = [[2, 3]]
test_matrix4 = [[1], [2], [3]]
test_matrix5 = [[2, 5, 8], [4, 0, -1]]
print(solution.spiralOrder(test_matrix5))