def getStrength(password, weight_a):
  # Complete the function
  result = 0
  for letter in password:
    letter_weight = ord(letter) - 97 + weight_a
    if ord(letter) - 97 + weight_a <= 25:
      result += letter_weight
    else:
      result += letter_weight - 26
  return result


def main(inputFile, outputFile):
  securityInput = open(inputFile, 'r')
  securityOutput = open(outputFile, 'w')
  
  password = securityInput.readline().strip()
  weight_a = int(securityInput.readline().strip())
  
  securityOutput.write(f'{getStrength(password, weight_a)}\n')
  
  securityInput.close()
  securityOutput.close()


main('highSecurity.in', 'highSecurity.out')
