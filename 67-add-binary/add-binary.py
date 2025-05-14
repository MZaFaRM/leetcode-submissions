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
            result = 0
            if i >= m:
                result = int(inp[i])
            result += int(out[i]) + carry
            
            carry = result >= 2
            if result % 2 != 0:
                out[i] = "1"
            else:
                out[i] = "0"
            i -= 1
        out = "".join(out)
        if carry:
            return "1" + out
        else:
            return out