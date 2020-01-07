class Solution:
    def __init__(self, s:str):
        self.s = s
        self.count = {"Q": self.s.count('Q'), "W": self.s.count('W'), "E": self.s.count('E'), "R": self.s.count('R')}
        self.modify = {}

    def balanced_string(self):
        avg = len(self.s)//4
        for k, v in self.count.items():
            if v > avg:
                self.modify[k] = v - avg
        if self.modify == {}:
            # 已经平衡了
            return 0
        i = j = 0
        min_length = len(self.s)
        # substring = ""
        while j < len(self.s):
            if self.is_substring(self.s[i:j]):
                while self.is_substring(self.s[i:j]):
                    i += 1
                substring_len = len(self.s[i-1:j])
                if substring_len < min_length:
                    min_length = substring_len
                    # substring = self.s[i-1:j]
            else:
                j += 1
        return min_length  # , substring

    def is_substring(self, s:str):
        for v in self.modify.keys():
            if v in s and s.count(v) >= self.modify[v]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    # s = "WWEEEREWQWWRWWERQWEQ"
    # s = "QWER"
    # s = "QQWE"
    # s = "QQQW"
    s = "QQQQ"
    slt = Solution(s)
    print(slt.balanced_string())