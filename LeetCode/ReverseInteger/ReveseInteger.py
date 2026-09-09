class Solution(object):
    def reverse(self, x):
        val = str(x)
        sign = 1
        if val[0] == "-":
            sign = -1
            val = val[1:]

        val = val[::-1]

        val = int(val) * sign
        if -2 ** 31 < val < 2 ** 31 - 1:
            return val
        else:
            return 0
