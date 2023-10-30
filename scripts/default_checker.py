#!/usr/bin/python3

from os.path import abspath, join, realpath
from sys import stdin, stderr, path

path.append(abspath(join(realpath(__file__), '../..')))

from src.checker_base import CheckerBase

class DefaultChecker(CheckerBase):
    
    def check(self):
        # This checker assumes that input is well-formatted.
        # If you don't trust your formatting, add checks yourself.
        inp = self.input.decode().split('\n')
        n = int(inp[1])
        s = inp[2]
        out = self.output.decode().split('\n')
        k = int(out[0])
        if s.count('0') != s.count('1'):
            if k != -1:
                return ('False', 'Bruh')
            else:
                return ('True', 'OK')
        if k == 0:
            out.extend(['1'])
        for x in map(int, out[1].split(' ')):
            s = s[:x - 1] + '01' + s[x - 1:]
        for i in range(len(s) // 2):
            if s[i] == s[- i - 1]:
                return ('False', 'String is not good')
        return ('True', 'OK')
        # return super().check()
    
    def input(self):
        return super().input
    
    def output(self):
        return super().output


def main():
    dc = DefaultChecker()
    payload = stdin.read().rstrip().encode()
    dc.input, dc.output = payload.split(bytes([0x1C]))
    status, message = dc.check()
    if status:
        print('OK')
    else:
        print(message, file=stderr)
        print('WRONG_ANSWER')

if __name__ == '__main__':
    main()
