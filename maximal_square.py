"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

For example, given the following matrix:

1 0  1 0  0
1 0 (1 1) 1
1 1 (1 1) 1
1 0  0 1  0
Return 4.
"""

"""
Time Complexity: O(mn) -- iterate through entire matrix
Space Complexity: O(mn) -- use another matrix of same size

Explanation:
Dynamic programming. Keep track of max size square of 1s that can be made at
entry matrix[i][j]. This is determined by the following:
*   if entry is on the top or left border, the max square containing that entry has
    to be 1 or 0, since it's on the edge.
*   otherwise, max size square will be 1 more than the minimum of the square above,
    to the left, and topleft.
"""
def max_square(matrix):
    if len(matrix) == 0:
        return 0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_squares = list(matrix) # DP matrix should be same size as matrix
    max_square_size = 0
    for row in xrange(0,num_rows):
        for col in xrange(0,num_cols):
            # if entry is on the top or left border, the max square containing
            # that entry has to be 1 or 0, since it's on the edge.
            if row == 0 or col == 0:
                max_squares[row][col] = int(matrix[row][col])
            else:
                top = max_squares[row-1][col]
                topleft = max_squares[row-1][col-1]
                left = max_squares[row][col-1]
                if int(matrix[row][col]) != 0 and top > 0 and topleft > 0 and left > 0:
                    max_squares[row][col] = min(top, topleft, left) + 1
                else:
                    max_squares[row][col] = int(matrix[row][col])
            max_square_size = max(max_square_size, max_squares[row][col])
            col += 1
        row += 1
    return max_square_size*max_square_size

"""
My initial significantly slower non-DP solution.
1. Find largest possible size square. For a 5x4, this would be a 4x4 square.
2. Find each possible square of this size in the array, and check if it's all 1s.
3. If it is, return the area of this max size square.
4. Decrement max square size by 1 and repeat steps 2-4.
"""
def max_square_2(matrix):
    if len(matrix) == 0:
        return 0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_square_size = min(num_rows, num_cols)
    while max_square_size > 0:
        start_row = 0
        end_row = max_square_size
        while end_row <= num_rows:
            start_col = 0
            end_col = max_square_size
            while end_col <= num_cols
                if is_all_ones(matrix, start_row, end_row, start_col, end_col):
                    return max_square_size*max_square_size
                start_col += 1
                end_col += 1
            start_row += 1
            end_row += 1
        max_square_size -= 1
    return 0

def is_all_ones(matrix, start_row, end_row, start_col, end_col):
    for row in xrange(start_row, end_row):
        for col in xrange(start_col, end_col):
            if matrix[row][col] != '1':
                return False
    return True
