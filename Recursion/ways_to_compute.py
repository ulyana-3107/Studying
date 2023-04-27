class Solution(object):
    def diffWaysToCompute(self, expression: str):
        # operations map
        operation = {'*': lambda x, y: x*y, '+': lambda x, y: x+y, '-': lambda x, y: x-y}

        def helper(expression):
            result = []
            for i, x in enumerate(expression):
                if x in ('+', '-', '*'):
                    leftResult = helper(expression[0:i])  # list of results for the left expression(s)
                    rightResult = helper(expression[i+1:])  # list of results for the right expression(s)
                    # append all the combinations
                    for leftValue in leftResult:
                        for rightValue in rightResult:
                            result.append(operation[x](leftValue, rightValue))
            return result if result else [int(expression)]  # if result list is empty => expression is the single number
        return helper(expression)