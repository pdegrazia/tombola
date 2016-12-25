import random
import os

linea1 = [str(i).zfill(2) for i in range(1,11)]
linea2 = [str(i).zfill(2) for i in range(11,21)]
linea3 = [str(i).zfill(2) for i in range(21,31)]
linea4 = [str(i).zfill(2) for i in range(31,41)]
linea5 = [str(i).zfill(2) for i in range(41,51)]
linea6 = [str(i).zfill(2) for i in range(51,61)]
linea7 = [str(i).zfill(2) for i in range(61,71)]
linea8 = [str(i).zfill(2) for i in range(71,81)]
linea9 = [str(i).zfill(2) for i in range(81,91)]

linea1.insert(5,'\033[91m**\033[00m')
linea2.insert(5,'\033[91m**\033[00m')
linea3.insert(5,'\033[91m**\033[00m')
linea4.insert(5,'\033[91m**\033[00m')
linea5.insert(5,'\033[91m**\033[00m')
linea6.insert(5,'\033[91m**\033[00m')
linea7.insert(5,'\033[91m**\033[00m')
linea8.insert(5,'\033[91m**\033[00m')
linea9.insert(5,'\033[91m**\033[00m')

stars = ['\033[91m**\033[00m' for i in range(0,11)]

tabellone = [stars, linea1,linea2,linea3,stars,linea4,linea5,linea6, stars, linea7, linea8, linea9, stars]

numbers = [i for i in range(1,91)]


def print_tabellone():
    os.system('clear')
    for row in tabellone:
        for number in row:
            print number,
        print '\n'


def remove_from_tabellone(number):
    for i in range(0,len(tabellone)):
        for j in range(0,len(tabellone[i])):
            if str(number).zfill(2) == tabellone[i][j]:
                tabellone[i][j] = '\x1b[6;30;42m' + tabellone[i][j] + '\x1b[0m'

while True and len(numbers) > 0:
    option = raw_input('Press enter key to extract number')
    index = random.randint(0, len(numbers)-1)
    number = numbers[index]
    print 'number:', number
    numbers.pop(index)
    remove_from_tabellone(number)
    print_tabellone()


