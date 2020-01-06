from copy import deepcopy
class String:
    def __init__(self, string, words):
        self.string = string
        self.words = words
        self.word_length = len(self.words[0])
        self.result = []
        print(self.string)

    def process(self):
        length = len(self.string)
        i = 0   # 移动指针
        while i <= length:
            j = i  # 判断单词
            words = deepcopy(self.words)
            while self.string[j:j+self.word_length] in words:
                words.remove(self.string[j:j+self.word_length])
                j += self.word_length
            if len(words) == 0:
                self.result.append(i)
            i += 1
        return self.result

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    string = String(s, words)
    print(string.process())
