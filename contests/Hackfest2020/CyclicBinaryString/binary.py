def getMaxZeroStreaks(toss):
  maxStreak = 0
  curStreak = 0
  toss = toss + toss
  for t in toss:
    if t != '0':
      maxStreak = max(maxStreak, curStreak)
      curStreak = 0
    else:
      curStreak += 1
  return max(maxStreak, curStreak)


def maximumPower(s):
  strSet = {char for char in s}
  if len(strSet) == 1 and '1' not in strSet:
    return -1
  result = getMaxZeroStreaks(s)
  return result


def main(inputFile, outputFile):
  binaryInput = open(inputFile, 'r')
  binaryOutput = open(outputFile, 'w')

  s = binaryInput.readline().strip()

  binaryOutput.write('{}\n'.format(maximumPower(s)))

  binaryInput.close()
  binaryOutput.close()

main('binary.in', 'binary.out')