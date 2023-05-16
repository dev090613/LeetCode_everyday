class Solution:
    def isValid(self, s: str) -> bool:
        '''
        s: "( [ ) ] "
        c:      ^
        stack = [ '(' '['  ] # 닫히는 괄호가 stack[-1]일 때 제거되도록 한다
        '''
        stack = []
        closeToOpen = { ')':'(', ']':'[', '}':'{' }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
            
            
            