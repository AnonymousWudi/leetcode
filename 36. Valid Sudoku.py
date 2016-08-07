# coding=utf-8

"""
	question url: https://leetcode.com/problems/valid-sudoku/
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.check_row(board) and self.check_col(board) and self.check_square(board)
        
    def check_row(self, board):
        for x in board:
            if not self.check_valid(x):
                return False
        return True
    
    def check_col(self, board):
        for y in zip(*board):
            if not self.check_valid(y):
                return False
        return True
    
    def check_square(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.check_valid(square):
                    return False
        return True
    
    def check_valid(self, check_list):
        check_list = [i for i in check_list if i != '.']
        return len(set(check_list)) == len(check_list)