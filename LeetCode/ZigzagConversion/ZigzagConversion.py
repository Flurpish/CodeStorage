class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        new = ""
        spread = (numRows - 1) * 2

        for row in range(numRows):
            current = row

            while current < len(s):
                new += s[current]

                if row != 0 and row != numRows - 1:
                    diagonal = current + spread - (2 * row)

                    if diagonal < len(s):
                        new += s[diagonal]

                current += spread

        return new
