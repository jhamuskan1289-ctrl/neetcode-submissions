from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            a = [0] * 10
            for j in i:
                if j != ".":
                    a[int(j)] += 1
                    if a[int(j)] > 1:
                        return False

        for i in range(len(board)):
            a = [0] * 10
            for j in range(len(board)):
                x = board[j][i]
                if x != ".":
                    a[int(x)] += 1
                    if a[int(x)] > 1:
                        return False


        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                a = [0] * 10
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        x = board[k][l]
                        if x != ".":
                            a[int(x)] += 1
                            if a[int(x)] > 1:
                                return False

        return True



