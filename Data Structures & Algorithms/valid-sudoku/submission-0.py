class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
        #column
        for col in range(9):
            seen = set()
            for row_num in range(9):
                num = board[row_num][col]
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

        #cells
        boxes = {}
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    box_key = (row // 3, col // 3)
                    if box_key not in boxes:
                        boxes[box_key] = set()
                    if num in boxes[box_key]:
                        return False
                    boxes[box_key].add(num)
        

        return True
