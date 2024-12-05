###
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
###
def scanForXmas(board, r, c) -> int:
  BOARD_H, BOARD_W = len(board), len(board[0]) # slow
  # Check around for Ms and then proceed to try to build xmas on each axis with an M

  DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  # Bounds check happens by short circuiting before trying an access
  foundXmasCount = 0
  for dirPair in DIRECTIONS:
    dr, dc = dirPair[0], dirPair[1] # RISKY
    if isInBounds(r+dr, c+dc, BOARD_H, BOARD_W) and board[r+dr][c+dc] == "M":
      if tryBuildXmas(board, r+dr, c+dc, dr, dc):
        foundXmasCount += 1
  return foundXmasCount

def tryBuildXmas(board, r, c, dr, dc):
  BOARD_H, BOARD_W = len(board), len(board[0])
  # Gross
  aStepR, aStepC = r+dr, c+dc
  if not isInBounds(aStepR, aStepC, BOARD_H, BOARD_W) or board[aStepR][aStepC] != "A":
    return False
  sStepR, sStepC = aStepR+dr, aStepC+dc
  if not isInBounds(sStepR, sStepC, BOARD_H, BOARD_W) or board[sStepR][sStepC] != "S":
    return False
  return True

def tryBuildMas(board, r, c):
  BOARD_H, BOARD_W = len(board), len(board[0])
  # Bounds check
  if not isInBounds(r-1, c-1, BOARD_H, BOARD_W) or not isInBounds(r-1, c+1, BOARD_H, BOARD_W) or not isInBounds(r+1, c-1, BOARD_H, BOARD_W) or not isInBounds(r+1, c+1, BOARD_H, BOARD_W):
    return False
  # \ M S or S M
  if not (board[r-1][c-1] == "M" and board[r+1][c+1] == "S") and not (board[r-1][c-1] == "S" and board[r+1][c+1] == "M"):
    return False

  # / M S or S M
  if not (board[r+1][c-1] == "M" and board[r-1][c+1] == "S") and not (board[r+1][c-1] == "S" and board[r-1][c+1] == "M"):
    return False
  return True

def isInBounds(r, c, BOARD_H, BOARD_W) -> bool:
  return r >= 0 and c >= 0 and r < BOARD_H and c < BOARD_W

def PartOne(board: list):
  xmasCount = 0
  for r in range(len(board)):
    for c in range(len(board[0])):
      if board[r][c] == "X":
        xmasCount += scanForXmas(board, r, c)
  print(xmasCount)


def PartTwo(board: list):
  xmasCount = 0
  for r in range(len(board)):
    for c in range(len(board[0])):
      if board[r][c] == "A" and tryBuildMas(board, r, c):
        xmasCount += 1
  print(xmasCount)

def main():
  boardLineList = open("day4.input.txt").readlines()
  # boardLineList = open("day4.sample.txt").readlines()
  boardList = []
  for line in boardLineList:
    boardList.append(list(line.strip()))

  # PartOne(boardList)
  PartTwo(boardList)

main()