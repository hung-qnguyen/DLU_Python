#1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2
import platform
print('Current Python version: ',platform.python_version())

#3
import datetime
now = datetime.datetime.now()
print ("Current datetime: ", now.strftime("%Y-%m-%d %H:%M:%S"))

# 4
r = float(input('Radius: '))
print('Area: ', str(pi * r ** 2))

# 5
firstName = input('First Name: ')
lastName = input('Last Name: ')
print('Your Name: {0} {1}'.format(lastName, firstName))

# 6
squenceNumbers = input('Enter sequence of numbers, separated by comma: ')
listOfNumbers = squenceNumbers.split(',')
tupleOfNumbers = tuple(listOfNumbers)
print('List: ', listOfNumbers)
print('Tuple: ', tupleOfNumbers)

# 7
filename = input('Enter your file name: ')
extension = filename.split('.')[-1]
print('Your file name extension: ', extension)

# 8 
colorList = ["Red", "Green", "White", "Black"]
print('First colors in list: ', colorList[0])
print('Last colors in list: ', colorList[-1])

# 9
examDate = (11, 12, 2023)
print('The examination will start from: %i/ %i/ %i' % examDate)

# 10
n = 5
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print('The value of n+nn+nnn: ', n1 + n2 + n3)

# 11
print(abs.__doc__)

# 12
import calendar
m = int(input('Enter month: '))
y = int(input('Enter year: '))
print(calendar.month(y, m))

#   13
sample_string = '''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example '''

print(sample_string)

#  14. Write a Python program to calculate number of days between two
#  dates.
from datetime import date

firstDay = date(2014, 7, 2)
lastDay = date(2014, 7, 11)
diff = lastDay.day - firstDay.day
print('{0} days between first and last'.format(diff))

#  15. Write a Python program to get the volume of a sphere with radius 6.
from math import pi
radius = 6
volume = 4.0 / 3.0 * pi * radius ** 3
print('The volume of a sphere: ', volume)

#  16
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
print(difference(10))
print(difference(53))

#  17
def nearThousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
print(nearThousand(3600))
print(nearThousand(256))


#  18
def sumOfThree(a, b, c):
    sums = a + b + c
    if a == b == c:
        sums = sums * 3
    return sums

print(sumOfThree(1, 2, 3))


#  19
def addIsToString(s):
    if len(s) >= 2 and s[:2] == "Is":
        return s
    return "Is " + s

print(addIsToString('Hello world'))


#  20
def copyString(s, count):
    result = ""
    for i in range(count):
        result += s
    return result

print(copyString('long', 10))

#  21
num = int(input('Enter your number: '))
if num & 1 == 1:
    print('Odd')
else:
    print('Even')

#  22
givenList1 = [1, 2, 3, 4, 5, 6, 3, 3, 2, 4]
def countThe4s(argList):
    count = 0
    for i in range(len(argList)):
        if argList[i] == 4:
            count += 1
    return count

print(countThe4s(givenList1))


#  23
def copySubstring(s, amount):
    substring = ""
    if len(s) < 2:
        substring = s[:len(s)]
    else:
        substring = s[:2]

    result = ""
    for i in range(amount):
        result += substring

    return result

print(copySubstring('testing', 5))


#  24. Write a Python program to test whether a passed letter is a vowel
#  or not.
def validateVowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(validateVowel('c'))
print(validateVowel('e'))

#  25
givenList2 = [1, 2, 3, 4, 5, 6, 7, 2, 3]

def isInGroup(num, listIn):
    for i in range(len(listIn)):
        if listIn[i] == num:
            return True
    return False
print(isInGroup(12, givenList2))
