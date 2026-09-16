roman = {
        "1": "I",
        "5": "V",
        "10": "X",
        "50": "L",
        "100": "C",
        "500": "D",
        "1000": "M"
    }

class Solution(object):

    def intToRoman(self, num):
        
        num = str(num)
        length = len(num)
        val = ""

        for i in num:
            val += self.getRoman(i, length)
            length -= 1
        
        return val

    def getRoman(self, num, place):
        num = int(num)
        val = ""
        exp = 10**(place-1)

        if place == 4:
            return roman["1000"] * num
        else:
            if num == 4 or num == 9:
                return roman[str(exp)] + roman[str(num*(exp) + exp)]
            else:
                while num != 0:
                    if num >= 5:
                        val += roman[str(5*(exp))]
                        num -= 5
                    else:
                        val += roman[str(1*(exp))]
                        num -= 1
                return val

        
