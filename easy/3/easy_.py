class Solution(object):
    def __init__(self):
        self.array = []
    def totalMoney(self, n):
        temp_monday = 1
        temp_sum = 0
        temp_day = 0
        sum = 0
        while sum != n and sum < n:
            temp_day += 1
            if temp_day > 7:
                temp_monday += 1
                temp_sum = temp_monday - 1
                temp_day = 1
            temp_sum += 1
            self.array.append(temp_sum)
            sum += temp_sum
            print(self.array)

    def pprint(self):
        res = ''
        for i in range(len(self.array)-1):
            if self.array[i] % 7 == 0:
                res += str(self.array[i]) + ')'
            else:
                res += str(self.array[i])
            print(res)



a = Solution()
a.totalMoney(80)
a.pprint()



