class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        for curr_day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                temp_day = stack.pop()
                result[temp_day] = curr_day - temp_day
            stack.append(curr_day)
        return result

        