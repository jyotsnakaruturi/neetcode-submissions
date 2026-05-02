class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=s.lower()
        S=""
        for i in l:
            if i.isalnum():
                S+=i
        n=len(l)
        if S==S[::-1]:
            return True
        else:
            return False

        