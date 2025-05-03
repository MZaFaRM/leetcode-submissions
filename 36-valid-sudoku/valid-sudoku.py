class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        i = 0
        j = 0
        column = {k: set() for k in range(9)}
        box = {k: set() for k in range(9)}
        while i < size:
            row = set()
            while j < size:
                val = board[i][j]
                grp = ((i//3)*3)+(j//3)
                if val == ".":
                    pass
                elif val in row:
                    return False
                elif val in column[j]:
                    return False
                elif val in box[grp]:
                    return False
                else:
                    row.add(val)
                    column[j].add(val)
                    box[grp].add(val)
                j += 1
            j = 0
            i += 1
        return True