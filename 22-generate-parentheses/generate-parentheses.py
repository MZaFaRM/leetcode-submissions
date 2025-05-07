class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.search = []
        self.backtrack(n, n)
        return ["".join(solution) for solution in self.result]

    def backtrack(self, left, right):
        if right == 0:
            self.result.append(self.search[:])

        elif left == 0:
            self.search.append(")")
            self.backtrack(left, right - 1)
            self.search.pop()

        elif left == right:
            self.search.append("(")
            self.backtrack(left - 1, right)
            self.search.pop()

        elif left < right:
            self.search.append("(")
            self.backtrack(left - 1, right)
            self.search.pop()
            
            self.search.append(")")
            self.backtrack(left, right - 1)
            self.search.pop()
        