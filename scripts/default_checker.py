#!/usr/bin/python3

from os.path import abspath, join, realpath
from sys import stdin, stderr, path

path.append(abspath(join(realpath(__file__), '../..')))

from src.checker_base import CheckerBase

class DefaultChecker(CheckerBase):
    
    def check(self):
        return super().check()
    
    def input(self):
        return super().input
    
    def output(self):
        return super().output


def main():
    dc = DefaultChecker()
    payload = stdin.read().rstrip(' \n\t').encode()
    dc.input, dc.output = payload.split(bytes([0x1C]))
    status, message = dc.check()
    if status:
        print('OK')
    else:
        print(message, file=stderr)
        print('WRONG_ANSWER')

if __name__ == '__main__':
    main()
