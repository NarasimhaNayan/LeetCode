class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s :
            if len(stack) > 0 :
                if ((stack[-1] == '[' and bracket == ']') or (stack[-1] == '{' and bracket == '}') 
                or (stack[-1] == '(' and bracket == ')')) :
                    stack.pop()
                else :
                    # top+=1
                    stack.append(bracket)
            else :
                stack.append(bracket)

        return False if len(stack) else True

        