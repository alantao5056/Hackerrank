def getWinningPlayerByNum(number1, number2):
  if number1 > number2:
    return '1'
  if number1 < number2:
    return '2'
  return 'draw'


def getRoundResult(winning_suit, suit1, number1, suit2, number2):
  # Write your code here
  if suit1 == winning_suit:
    if suit2 != winning_suit:
      return 'Player 1 wins'
    else:
      winningByNum = getWinningPlayerByNum(number1, number2)
      if winningByNum != 'draw':
        return f'Player {winningByNum} wins'
      else:
        return 'draw'
  else:
    if suit2 == winning_suit:
      return 'Player 2 wins'
    else:
      winningByNum = getWinningPlayerByNum(number1, number2)
      if winningByNum != 'draw':
        return f'Player {winningByNum} wins'
      else:
        return 'Draw'


def getWinner(log, winning_suit):
  result = ''
  for l in log:
    result += getRoundResult(winning_suit, l[0], l[1], l[2], l[3]) + '\n'

  return result


def main(inputFile, outputFile):
  winnerInput = open(inputFile, 'r')
  winnerOutput = open(outputFile, 'w')

  winning_suit = winnerInput.readline().strip()
  N = int(winnerInput.readline().strip())
  log = []

  for _ in range(N):
    line = winnerInput.readline().strip().split()
    log.append([line[0], int(line[1]), line[2], int(line[3])])

  winnerOutput.write(getWinner(log, winning_suit))

  winnerInput.close()
  winnerOutput.close()


main('winner.in', 'winner.out')
