def processLine(nums: list):
  desc = int(nums[0]) > int(nums[1])
  for i in range(len(nums) - 1): # off-by-one to help with right bounds check
    this, next = int(nums[i]), int(nums[i+1])
    if (desc and this <= next) or ((not desc) and this >= next):
      return False
    elif abs(this - next) > 3:
      return False
  return True

def processLineWithTolerance(nums: list):
  if processLine(nums):
    return True
  for removali in range(len(nums)):
    # If a removal works, return true. If there are NO working removals, then return False
    # Big efficiency for simplicity tradeoff: Brute force removing levels
    numsRemoved = nums.copy()
    numsRemoved.pop(removali)
    reportSafe = processLine(numsRemoved)
    if reportSafe:
      return True
  return False

def main():
  safetyCount = 0
  inputFile = open("day2.input.txt")
  # inputFile = open("day2.sample.txt")
  for line in inputFile:
    nums = line.split()
    for i in range(len(nums)):
      nums[i] = int(nums[i])
    if processLineWithTolerance(nums):
      safetyCount += 1
  print(safetyCount)


main()