


def main():
  distance = 0
  similarityScore = 0
  leftList, rightList = [], []
  inputFile = open("day1input")
  # inputFile = open("day1inputSAMPLE")
  for line in inputFile:
    leftVal, rightVal = line.split()
    leftList.append(int(leftVal))
    rightList.append(int(rightVal))
  leftList.sort()
  rightList.sort()
  rightFreqs = {}
  for num in rightList:
    if num in rightFreqs:
      rightFreqs[num] += 1
    else:
      rightFreqs[num] = 1

  for num in leftList:
    if num in rightFreqs:
      similarityScore += num * rightFreqs[num]

  print(similarityScore)


main()