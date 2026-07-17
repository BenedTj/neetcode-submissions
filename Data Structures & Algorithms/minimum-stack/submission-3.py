class MinStack:

    def __init__(self):
        self.st = []
        self.leng = 0
        
        self.curmin = math.inf

    def push(self, val: int) -> None:
        self.curmin = min(self.curmin, val)
        self.st.append((val, self.curmin))
        self.leng += 1

    def pop(self) -> None:
        self.st.pop()
        self.leng -= 1

        if self.leng == 0:
            self.curmin = math.inf
        else:
            self.curmin = self.st[self.leng - 1][1]

    def top(self) -> int:
        return self.st[self.leng - 1][0]

    def getMin(self) -> int:
        return self.st[self.leng - 1][1]
