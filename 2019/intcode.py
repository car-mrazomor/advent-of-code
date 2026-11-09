from collections import defaultdict


class Intcode:
    def __init__(self, program, inputs=()):
        self.mem = defaultdict(int, enumerate(program))
        self.ip = self.base = 0
        self.inputs = list(inputs)
        self.halted = False

    @classmethod
    def load(cls, text, inputs=()):
        return cls([int(x) for x in text.strip().split(",")], inputs)

    def addr(self, n):
        mode = self.mem[self.ip] // 10 ** (n + 1) % 10
        if mode == 0:
            return self.mem[self.ip + n]
        if mode == 1:
            return self.ip + n
        return self.base + self.mem[self.ip + n]

    def run(self, *inputs):
        self.inputs += inputs
        out, m = [], self.mem
        while True:
            op = m[self.ip] % 100
            if op == 99:
                self.halted = True
                return out
            a, b, c = self.addr(1), self.addr(2), self.addr(3)
            if op == 1:
                m[c] = m[a] + m[b]
                self.ip += 4
            elif op == 2:
                m[c] = m[a] * m[b]
                self.ip += 4
            elif op == 3:
                if not self.inputs:
                    return out
                m[a] = self.inputs.pop(0)
                self.ip += 2
            elif op == 4:
                out.append(m[a])
                self.ip += 2
            elif op == 5:
                self.ip = m[b] if m[a] else self.ip + 3
            elif op == 6:
                self.ip = m[b] if not m[a] else self.ip + 3
            elif op == 7:
                m[c] = int(m[a] < m[b])
                self.ip += 4
            elif op == 8:
                m[c] = int(m[a] == m[b])
                self.ip += 4
            elif op == 9:
                self.base += m[a]
                self.ip += 2
            else:
                raise ValueError(f"unknown opcode {op} at {self.ip}")
