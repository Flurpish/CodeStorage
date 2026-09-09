#This one was pretty hard

class Solution(object):
    def isMatch(self, s, p):
        
        memo = {}

        def match(i, j):
    
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == ".")
            )

            if j + 1 < len(p) and p[j + 1] == "*":

                skip = match(i, j + 2)

                use = first_match and match(i + 1, j)

                memo[(i, j)] = skip or use

            else:
                memo[(i, j)] = (
                    first_match and match(i + 1, j + 1)
                )

            return memo[(i, j)]

        return match(0, 0)
