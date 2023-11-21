def clumsy(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        stack = [n]
        ops = 0 
        
        for i in range(n-1, 0, -1):
            if ops % 4 == 0:
                stack[-1] *= i
            elif ops % 4 == 1:
                stack[-1] = int(stack[-1] / i)
            elif ops % 4 == 2:
                stack.append(i)
            elif ops % 4 == 3:
                stack.append(-i)
            
            ops += 1
        
        return sum(stack)
