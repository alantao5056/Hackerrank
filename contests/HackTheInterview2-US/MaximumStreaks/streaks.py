def getMaxHeadStreaks(toss):
  maxStreak = 0
  curStreak = 0
  for t in toss:
    if t != 'Heads':
      maxStreak = max(maxStreak, curStreak)
      curStreak = 0
    else:
      curStreak += 1
  return max(maxStreak, curStreak)


def getMaxTailStreaks(toss):
  maxStreak = 0
  curStreak = 0
  for t in toss:
    if t != 'Tails':
      maxStreak = max(maxStreak, curStreak)
      curStreak = 0
    else:
      curStreak += 1
  return max(maxStreak, curStreak)


def getMaxStreaks(toss):
  # Return an array of two integers containing the maximum streak of heads and tails respectively
  return [getMaxHeadStreaks(toss), getMaxTailStreaks(toss)]


def main(inputFile, outputFile):
  streaksInput = open(inputFile, 'r')
  streaksOutput = open(outputFile, 'w')

  N = int(streaksInput.readline().strip())
  log = []

  for _ in range(N):
    log.append(streaksInput.readline().strip())

  result = getMaxStreaks(log)
  streaksOutput.write(f'{result[0]} {result[1]}\n')

  streaksInput.close()
  streaksOutput.close()


main('streaks.in', 'streaks.out')
