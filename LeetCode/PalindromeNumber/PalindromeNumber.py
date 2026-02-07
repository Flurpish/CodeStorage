class Solution(object):
    def isPalindrome(self, x):
        
        value = list(str(x))
        palindrome = list(str(x))
        palindrome.reverse()
            
        return value == palindrome
    
# Best case for speed
#class Solution(object):
#    def isPalindrome(self, x):
#        if x < 0:
#            return False
#
#        s = str(x)
#        return s == s[::-1] ::-1 is syntax to reverse a string