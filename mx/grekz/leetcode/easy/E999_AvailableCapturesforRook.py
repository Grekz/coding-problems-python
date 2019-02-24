'''
@author: grekz
'''


class E999_AvailableCapturesforRook:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rows, cols, ans, posR, posC = len(board), len(board[0]), 0, 0, 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'R':
                    posR = i
                    posC = j
                    break

        for i in range(posR + 1, rows):
            if board[i][posC] != '.':
                if board[i][posC] == 'p':
                    ans += 1
                break

        for i in range(posR - 1, -1, -1):
            if board[i][posC] != '.':
                if board[i][posC] == 'p':
                    ans += 1
                break

        for i in range(posC + 1, cols):
            if board[posR][i] != '.':
                if board[posR][i] == 'p':
                    ans += 1
                break

        for i in range(posC - 1, -1, -1):
            if board[posR][i] != '.':
                if board[posR][i] == 'p':
                    ans += 1
                break

        return ans
