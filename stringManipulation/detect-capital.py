# Given a string return true if the usage of capitals is correct
# word = "USA"
# return True
# word = "FLaG"
# return Flase
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle
