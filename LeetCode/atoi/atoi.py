#Not being allowed to use int type cast is monsterous (not that bad just looks gross)
class Solution(object):
    def myAtoi(self, s):
        val = s.strip()
        if not val:
            return 0
            
        sign = [1, -1][val[0] == "-"]

        if val[0] in "-+":
            val = val[1:]

        digits = ""
        for char in val:
            if not char.isdigit():
                break
            digits += char

        if not digits:
            return 0

        val = 0

        for char in digits:
            val = val * 10 + (ord(char) - ord("0"))

        val *= sign

        if val < -2**31:
            return -2**31
        elif val > 2**31 - 1:
            return 2**31 - 1
        else:
            return val
        
