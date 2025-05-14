class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            out = list(a)
            inp = b
        else:
            out = list(b)
            inp = a

        i = -1
        carry = 0
        n = -len(out)
        m = -len(inp)

        while i >= n:
            result = int(inp[i]) if i >= m else 0
            result += int(out[i]) + carry
            carry = result >= 2
            out[i] = str(int(result % 2 != 0))
            i -= 1

        out = "".join(out)
        return "1" + out if carry else out