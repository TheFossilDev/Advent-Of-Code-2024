import re

def partOne():
  # searchString = open("day3.sample.txt").read()
  searchString = open("day3.input.txt").read()
  multiList = re.findall("mul\([1-9]+[0-9]*,[1-9]+[0-9]*\)", searchString)
  multiSum = 0
  for operation in multiList:
    x, y = int(operation.split(",")[0][4:]), int(operation.split(",")[1][0:-1])
    multiSum += x * y
  print(multiSum)

def partTwo():
  # searchString = open("day3part2.sample.txt").read()
  searchString = open("day3.input.txt").read()
  multiList = re.findall("(?:mul\([1-9][0-9]*,[1-9][0-9]*\)|do\(\)|don't\(\))", searchString)
  multiSum, multiActive = 0, True
  for operation in multiList:
    if operation == "do()":
      multiActive = True
      continue
    elif operation == "don't()":
      multiActive = False
      continue
    if multiActive:
      x, y = int(operation.split(",")[0][4:]), int(operation.split(",")[1][0:-1])
      multiSum += x * y
  print(multiSum)

def main():
  # partOne()
  partTwo()

main()