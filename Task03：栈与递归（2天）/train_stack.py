class Train:
    def __init__(self, train, k):
        self.Train = train
        self.H = []
        for i in range(k):
            self.H.append([])

    def train_entry(self, stations):

        for out in range(stations):
            print("当前站为{}".format(out+1))
            print("列车状态", self.Train)
            if self.Train[-1] == out+1:
                self.Train.pop()
            else:
                self.train_cache(stations, out)
            print("\t{}号车厢直接出站".format(out + 1))

    def train_cache(self, s, out):
        for _ in range(s):
            temp = self.Train.pop()
            i = 0
            for h in self.H:
                i += 1
                if h == [] or h[-1] < temp:
                    h.append(temp)
                    print("\t{}车厢出H{}".format(temp, i))
                    break
        for i in range(s, out+1, -1):
            self.Train.append(i)

if __name__ == '__main__':
    train = Train([5, 6, 1, 4, 3, 2], 3)
    train.train_entry(6)