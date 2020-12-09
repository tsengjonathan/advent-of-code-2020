class Instruction:
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg
        self.visited = False

        self.read_only_op = op
        self.read_only_arg = arg

    def __repr__(self):
        return f'Instruction(op={self.op}, arg={self.arg}, visited={self.visited})'

    def reset(self):
        self.visited = False
        self.op = self.read_only_op
        self.arg = self.read_only_arg

    def get_original(self):
        return f'{self.read_only_op} {self.read_only_arg}'
