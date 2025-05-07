class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.backtrack(n, n, []))

    def backtrack(self, left, right, current):
        if right == 0:
            yield "".join(current)
            return
        if left > 0:
            current.append("(")
            yield from self.backtrack(left-1, right, current)
            current.pop()
        if left < right:
            current.append(")")
            yield from self.backtrack(left, right-1, current)
            current.pop()