class Solution():
    def __init__(self, num:str):
        self.num = num

    def largestOddNumber(self):
        self.num = int(self.num)
        if self.num%2 == 1:
            pass
        else:
            self.num = list(str(self.num))
            temp = 0
            for i in self.num:
                if int(i) % 2 == 1 and int(i) > temp:
                    self.num = int(i)
        if isinstance(self.num,list):
            self.num = ''


    def PrintOddNumber(self):
        print(self.num)

num = Solution("42")
num.largestOddNumber()
num.PrintOddNumber()



