def isSafe(board, row, col, n):
  # for horizontal checking
  for j in range(col):
    if board[row][j] == 'Q':
      return False
    
  # for vertical checking
  for i in range(row):
    if board[i][col] == 'Q':
      return False
      
  # for left diagonal
  i, j = row - 1, col - 1
  while i >= 0 and j >= 0:
    if board[i][j] == 'Q':
      return False
    
    i -= 1
    j -= 1
    
  # for right diagonal
  i, j = row - 1, col + 1
  while i >= 0 and j < n:
    if board[i][j] == 'Q':
      return False
    
    i -= 1
    j += 1

  return True

def nQueens(board, ans, row, n):
  if row == n:
    ans.append(["".join(r) for r in board])
    return

  for col in range(n):
    if (isSafe(board, row, col, n)):
      board[row][col] = 'Q'
      nQueens(board, ans, row + 1, n)
      board[row][col] = '.'

n = 8
board = [['.' for _ in range(n)] for _ in range(n)]
ans = []

nQueens(board, ans, 0, n)

print("Total Solutions: ", len(ans))

i = 1
for solution in ans[:3]:  # Show only first 3 solutions
  print (f"Solution {i}:")
  for row in solution:
    for cell in row:
      print(cell, end=" ")
    print()
  print()
  i += 1