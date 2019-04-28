'''
@author: grekz
'''
class E0946_ValidateStackSequences:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped) :
            return False
        n, j, stack = len(pushed), 0, []
        for x in pushed:
            stack.append(x)
            while len(stack) and j < n and stack[-1] == popped[j] :
                j += 1
                stack.pop()
        return j == n