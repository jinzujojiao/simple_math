import random
#from docx import Document


class Calculation:
    max = 5
    addAmount = 50
    minusAmount = 50
    addList = []
    minusList = []
    ITEM_LEN = 37

    def __init__(self, max=5, addAmount=50, minusAmount=50):
        self.max = max
        self.addAmount = addAmount
        self.minusAmount = minusAmount

    def add(self):
        candidates = set()
        for i in range(0, self.max+1):
            j = self.max - i
            for k in range(0, j+1):
                candidates.add(str(i)+' + '+str(k)+' =')
        #print(candidates)
        self.addList = random.sample(candidates, k=self.addAmount)

    def minus(self):
        candidates = set()
        for i in range(0, self.max+1):
            for j in range(0, i+1):
                candidates.add(str(i) + ' - ' + str(j) + ' =')
        #print(candidates)
        self.minusList = random.sample(candidates, k=self.minusAmount)

    def print(self):
        arr = self.addList + self.minusList
        arr = random.sample(arr, len(arr))
        i = 0
        line = ''
        for item in arr:
            line += item + '                 \t'
            if 3 == i:
                print(line)
                print()
                i = 0
                line = ''
            else:
                i += 1
