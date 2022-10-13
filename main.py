import sys


class Main:
    def __init__(self):
        self.mem_size = 100000
        self.memory = [0] * 100000
        self.bracket_map = [0] * 100000
        self.stack = []
        self.data_ptr = 0
        self.inst_ptr = 0

    def run(self, code):
        commands = code.split()

        for pos, symbol in enumerate(commands):
            if symbol == 'xd':
                self.stack.append(pos)
            elif symbol == 'lol':
                last_open_pos = self.stack.pop()
                self.bracket_map[pos] = last_open_pos
                self.bracket_map[last_open_pos] = pos

        while self.inst_ptr < len(commands):
            command = commands[self.inst_ptr]
            match command:
                case "ha":
                    self.left()
                case "haha":
                    self.right()
                case "hahaha":
                    self.plus()
                case "hahahaha":
                    self.minus()
                case "lookatthat":
                    self.print()
                case "wtf":
                    self.input()
                case "xd":
                    self.start()
                case "lol":
                    self.stop()
            self.inst_ptr += 1

    def left(self):
        self.data_ptr = (self.data_ptr - 1) % self.mem_size

    def right(self):
        self.data_ptr = (self.data_ptr + 1) % self.mem_size

    def plus(self):
        self.memory[self.data_ptr] += 1

    def minus(self):
        self.memory[self.data_ptr] -= 1

    def print(self):
        print(chr(self.memory[self.data_ptr]), end='')

    def input(self):
        letter = input()
        self.memory[self.data_ptr] = ord(letter[0]) if letter else 0

    def start(self):
        if not self.memory[self.data_ptr]:
            self.inst_ptr = self.bracket_map[self.inst_ptr]

    def stop(self):
        if self.memory[self.data_ptr]:
            self.inst_ptr = self.bracket_map[self.inst_ptr]


def main() -> None:
    virtualmachine = Main()

    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            code = file.read()
        virtualmachine.run(code)
    else:
        print(f'usage: {sys.argv[0]} file.bh')


if __name__ == '__main__':
    main()
