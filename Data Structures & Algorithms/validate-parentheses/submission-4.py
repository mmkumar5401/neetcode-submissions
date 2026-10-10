class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            if i=='}':
                if not stack or not stack[-1]=='{':
                    return False
                else:
                    stack.pop(-1)
            elif i==']':
                if not stack or not stack[-1] =='[':
                    return False
                else:
                    stack.pop(-1)
            elif i==')':
                if not stack or not stack[-1] =='(':
                    return False
                else:
                    stack.pop(-1)
        if len(stack)==0:
            return True
        return False
        