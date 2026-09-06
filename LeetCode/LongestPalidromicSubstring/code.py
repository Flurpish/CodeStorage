class Solution(object):
    def longestPalindrome(self, s):
        current = s[0]

        for i in range(len(s)):
            indices = [x for x, letter in enumerate(s) if letter == s[i]]
            indices = indices[::-1]

            if len(indices) == 1:
                continue
            else:
                for j in range(len(indices)):
                    string = s[i:indices[j]+1]
                    if string == string[::-1] and len(string) > len(current):
                        current = string

        return current

#Pretty bad implementation tbh, it's in optimal speeds. At least it works!