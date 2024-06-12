# Python 3.9.2

def count_mines(board):
    rows = len(board)
    cols = len(board[0])
    
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),         (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    
    result_board = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1 or board[row][col] == 0:
                if board[row][col] == 1:
                    result_board[row][col] = 9
                else:
                    mine_count = 0
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if 0 <= r < rows and 0 <= c < cols and board[r][c] == 1:
                            mine_count += 1
                    result_board[row][col] = mine_count
            else:
                return "invalid input"

    return result_board

# Example usage:
board = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

result = count_mines(board)
for row in result:
    print(row)
