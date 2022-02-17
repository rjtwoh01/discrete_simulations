class Tank(object):
    def __init__(self):
        self.a = 0
        self.fin = 0
        self.fout = 0
        self.height = 0
        self.heightDiff = []
        self.heightList = []
        self.averageHeight = 0
        self.maxHeight = 0
        self.averageHeightDiff = 0
        self.maxHeightDiff = 0

    def getHeight(self):
        heightDifference = (self.fin - self.fout) / self.a
        self.heightDiff.append(heightDifference)
        self.height = self.height + heightDifference
        self.heightList.append(self.height)

    def calculateStats(self):
        self.maxHeight = max(self.heightList)
        self.averageHeight = sum(self.heightList) / len(self.heightList)
        self.maxHeightDiff = max(self.heightDiff)
        self.averageHeightDiff = sum(self.heightDiff) / len(self.heightDiff)


def main():
    tank1 = Tank(); tank2 = Tank()
    a = float(input('Enter area for tank 1: '))
    fin = float(input('Enter flow in for tank 1: '))
    fout = float(input('Enter flow out for tank 1: '))
    h = float(input('Enter starting height for tank 1: '))
    tank1.a = a; tank1.fin = fin; tank1.fout = fout; tank1.height = h
    a = float(input('Enter area for tank 2: '))
    fin = float(input('Enter flow in for tank 2: '))
    fout = float(input('Enter flow out for tank 2: '))
    h = float(input('Enter starting height for tank 2: '))
    tank2.a = a; tank2.fin = fin; tank2.fout = fout; tank2.height = h

    length = int(input('Enter the length of the simulation: '))
    i = 0
    
    while i < length:
        tank1.getHeight()
        tank2.getHeight()
        i += 1
        if (tank1.height <= 0 or tank2.height <= 0): break;
    
    tank1.calculateStats(); tank2.calculateStats()

    print('Tank 1: Average height:', tank1.averageHeight, "Max Height:", tank1.maxHeight, "Max Height Diff:", tank1.maxHeightDiff, "Avg Height Diff:", tank1.averageHeightDiff)
    print('Tank 2: Average height:', tank2.averageHeight, "Max Height:", tank2.maxHeight, "Max Height Diff:", tank2.maxHeightDiff, "Avg Height Diff:", tank2.averageHeightDiff)

if __name__ == "__main__":
    main()