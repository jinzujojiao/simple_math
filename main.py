# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from calculation import Calculation

def main(argv):
    max = int(argv[0])
    addAmount = int(argv[1])
    minusAmount = int(argv[2])
    cal = Calculation(max, addAmount, minusAmount)
    cal.add()
    cal.minus()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
