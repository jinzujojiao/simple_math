from random import randrange


class Calculation:
    max = 5
    addAmount = 50
    minusAmount = 50

    def __init__(self, max=5, addAmount=50, minusAmount=50):
        self.max = max
        self.addAmount = addAmount
        self.minusAmount = minusAmount

    def add(self):
        i = 0
        lastPart1 = -1
        lastPart2 = -1
        while i < self.addAmount:
            part1 = randrange(self.max+1)
            delta = self.max - part1
            part2 = randrange(0, delta+1)
            if (part1 != lastPart1) \
                and (part1 != lastPart2) \
                and (part2 != lastPart1) \
                and (part2 != lastPart2):
                print(f'{part1} + {part2} =                    ')
                lastPart1 = part1
                lastPart2 = part2
                i += 1

    def minus(self):
        i = 0
        lastNum1 = -1
        lastNum2 = -1
        while i < self.minusAmount:
            num1 = randrange(self.max + 1)
            num2 = randrange(0, num1 + 1)
            if (num1 != lastNum1) \
                    and (num2 != lastNum2):
                print(f'{num1} - {num2} =')
                lastNum1 = num1
                lastNum2 = num2
                i += 1