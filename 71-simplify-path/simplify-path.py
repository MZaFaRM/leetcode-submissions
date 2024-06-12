class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        dirs = path.split("/")
        for dir in dirs:
            if not dir or dir == ".":
                continue
            elif dir == "..":
                if stack: stack.pop()
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
            