class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            out = list(a)
            inp = list(b)
        else:
            out = list(b)
            inp = list(a)

        i = -1
        carry = 0
        n = -len(out)
        m = -len(inp)

        while i >= n:
            result = 0
            if i >= m:
                result = int(inp[i])
            result += int(out[i]) + carry

            if result == 3:
                carry = 1
                out[i] = "1"
            elif result == 2:
                carry = 1
                out[i] = "0"
            elif result == 1:
                carry = 0
                out[i] = "1"
            elif result == 0:
                carry = 0
                out[i] = "0"
            i -= 1
        out = "".join(out)
        if carry:
            return "1" + out
        else:
            return out