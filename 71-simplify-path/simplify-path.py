class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        dirs = path.split("/")
        for dr in dirs:
            if dr != '' and dr != ".":
                if dr == "..":
                    if stack: stack.pop()
                else:
                    stack.append(dr)

        return "/" + "/".join(stack)
            