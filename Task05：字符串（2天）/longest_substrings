class String:
    def __init__(self, string):
        self.string = string
        self.subs = []
        self.lenth = 0

    def process(self):
        i, j = 0, 0
        length = len(self.string)
        while j != length-1:
            j += 1
            while self.string[j] in self.string[i:j]:
                i += 1

            if j-i+1 > self.lenth:
                self.subs.clear()
                self.subs.append(self.string[i:j+1])
                self.lenth = j-i+1

            elif j-i+1 == self.lenth:
                self.subs.append(self.string[i:j+1])

        return self.subs, self.lenth

if __name__ == '__main__':
    string = "adbcabcdbb"
    s = String(string)
    print(s.process())
