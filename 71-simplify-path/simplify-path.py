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
                try:
                    stack.pop()
                except IndexError:
                    pass
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
            