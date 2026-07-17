class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        st = []

        for token in tokens:
            if token in ops:
                op2 = st.pop()
                op1 = st.pop()
                match token:
                    case "+":
                        st.append(op1 + op2)
                    case "-":
                        st.append(op1 - op2)
                    case "*":
                        st.append(op1 * op2)
                    case "/":
                        tmp = op1 / op2
                        if tmp >= 0:
                            tmp = math.floor(op1 / op2)
                        else:
                            tmp = math.ceil(op1 / op2)
                        st.append(tmp)
            else:
                st.append(int(token))
        
        return st[0]