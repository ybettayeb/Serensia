import unittest
from unittest.case import expectedFailure

def numberToDigits(number):
    return [int(x) for x in str(number)]

def computeCheckSum(digits):
    runningSum = 0
    EvenDigits = digits[0::2] # On commence à 0 avec un pas de 2
    oddDigits = digits[1::2] # On commence à 1 avec un pas de 2
    # print(EvenDigits,oddDigits)
    for digit in oddDigits: # là ou c'est sournois c'est qu'on compte à partir de l'index 1 en partant de la droite donc les nombres en position paire en index 0 
        #sont en position impaire en index 1
        prod = numberToDigits(digit*2)
        runningSum += sum(prod) 
    runningSum += sum(EvenDigits)
    return runningSum

def checkSiren(number):
    digits = numberToDigits(number)
    if len(digits) != 9:
        return False
    checkSum = computeCheckSum(digits)
    return checkSum % 10 == 0

def computeFullSiren(number):
    digits = numberToDigits(number)
    checksum = computeCheckSum(digits) % 10 
    if checksum == 0:
        res = str(number)+"0"
        return int(res) # double cast, c'est moche mais c'est le seul moyen de modifier un entier, je pourrais simplifier tout ça en restant avec des strings
    else:
        res = str(number)+ str(10 - checksum) # le chiffre de controle est égale à 10 - somme % 10 
        return int(res)


class testNumberToDigits(unittest.TestCase):
    def test_numberToDigitsSuccess(self):
        actual = numberToDigits(123456)
        expected = [1,2,3,4,5,6]
        self.assertEqual(actual,expected)
    def test_numberToDigitsZero(self):
        actual = numberToDigits(0)
        expected = [0]
        self.assertEqual(actual,expected)
class testCheckSiren(unittest.TestCase):
    def test_checkSiren(self):
        actual = checkSiren(414815217) #valid siren
        expected = True # 
        self.assertEqual(actual,expected)
    def test_checkSirenZero(self):
        actual = checkSiren(0)
        expected = False
        self.assertEqual(actual,expected)
    def test_checkSirenIncorrect(self):
        actual = checkSiren(414815216) #incorrect
        expected = False
        self.assertEqual(actual,expected)
class testCheckSum(unittest.TestCase):
    def test_computeCheckSumSimpleSuccess(self):
        actual = computeCheckSum([1,1,1,1])
        expected = 6
        self.assertEqual(actual,expected)
    def test_computeCheckSumZero(self):
        actual = computeCheckSum([0])
        expected = 0
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main()      
