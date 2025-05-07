class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.backtrack(n, n, "")
        return self.result

    def backtrack(self, left, right, current):
        if right == 0:
            self.result.append(current)
            return
        if left > 0:
            self.backtrack(left-1, right, current + "(")
        if left < right:
            self.backtrack(left, right-1, current + ")")