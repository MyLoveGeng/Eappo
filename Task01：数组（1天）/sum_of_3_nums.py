class Solution:
    def findthree(self, nums):
        nums_copy = sorted(nums)
        result = []
        length = len(nums)
        for i in range(length):
            for j in range(length-1, i, -1):
                nums_cut = nums_copy[i+1:j]
                temp = 0 - nums_copy[i] - nums_copy[j]
                if (temp in nums_cut) and ([nums_copy[i], temp, nums_copy[j]] not in result):
                    result.append([nums_copy[i], temp, nums_copy[j]])
        return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    result = s.findthree(nums)
    print(result)