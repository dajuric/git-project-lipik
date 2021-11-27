#based on the: https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
#take a look at the: https://codereview.stackexchange.com/questions/190101/expression-calculator-in-python/190370#190370

def calculate(s):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)           
            if op == "/": stack.append(int(stack.pop() / v))
    
        it, num, stack, sign = 0, 0, [], "+"
        
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":                                       
                num, j = calculate(s[it + 1:])
                it = it + j
            elif s[it] == ")":                                     
                update(sign, num)
                return sum(stack), it + 1
            it += 1
        update(sign, num)
        return sum(stack)

print(calculate("1+2*(3+3)"))