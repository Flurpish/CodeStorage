#Called submission.py because I don't want to have the filename be giant

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        seen = ""
        longest = ""

        for char in s:
            if char not in seen:
                seen += char
            else:
                if len(longest) < len(seen):
                    longest = seen
                _, seen = seen.split(char)
                seen += char

        if len(longest) < len(seen):
            return len(seen)

        return len(longest)


#Best speed submission
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         seen = {}
#         start = 0
#         max_len = 0
        
#         for end, char in enumerate(s):
#             # If the character is inside the current window, move the start pointer past its last seen index
#             if char in seen and seen[char] >= start:
#                 start = seen[char] + 1
            
#             # Store or update the character's last seen index
#             seen[char] = end
            
#             # Calculate current window length and update max_len
#             current_len = end - start + 1
#             if current_len > max_len:
#                 max_len = current_len
            
#         return max_len