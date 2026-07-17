class Solution:
    def isUnique(self, arr: List[str]) -> bool:
        prev = set({})

        for a in arr:
            if a.isnumeric():
                if a in prev:
                    return False
                prev.add(a)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            if not self.isUnique(row):
                return False
        
        # Check each column
        for col in range(len(board[0])):
            colarr = []
            for row in range(len(board)):
                colarr.append(board[row][col])
            
            if not self.isUnique(colarr):
                return False
        
        # Check each subbox
        upperleft = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (6, 3), (6, 0), (6, 3), (6, 6)]
        grids = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for x, y in upperleft:
            arr = list(map(lambda tupl: board[tupl[0] + x][tupl[1] + y], grids))

            if not self.isUnique(arr):
                return False
        
        return True