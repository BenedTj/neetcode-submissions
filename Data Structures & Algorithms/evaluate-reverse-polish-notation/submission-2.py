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
                        st.append(int(op1 / op2))
            else:
                st.append(int(token))
        
        return st[0]