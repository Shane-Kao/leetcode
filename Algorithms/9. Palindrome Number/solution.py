class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            return str(x) == str(x)[::-1]
        except:
            return False