#!/usr/bin/python3.11

from sys import stdin, stderr, path

path.append('/home/v1ctor/ws/dev/stress')

from src.checker_base import CheckerBase

class DefaultChecker(CheckerBase):
    
    def check(self) -> tuple[bool, str]:
        return super().check()
    
    def cpp_check(self) -> tuple[bool, str]:
        return super().cpp_check()
    
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
