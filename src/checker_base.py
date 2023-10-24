from abc import ABC, abstractmethod
from pathlib import Path
from subprocess import run
from sys import stderr


class CheckerBase(ABC):

    def __init__(self) -> None:
        self._input: None | bytes = None
        self._output: None | bytes = None

    @property
    @abstractmethod
    def input(self):
        return self._input

    @input.setter
    @abstractmethod
    def input(self, data: bytes):
        self._input = data

    @property
    @abstractmethod
    def output(self):
        return self._output

    @output.setter
    @abstractmethod
    def output(self, data: bytes):
        self._output = data

    @abstractmethod
    def cpp_check(self) -> tuple[bool, str]:
        base_data_path = Path().resolve() / 'data'
        if not (base_data_path / 'good').is_file():
            p_compile = run(f'g++ {base_data_path / "good.cpp"} -o {base_data_path / "good"}'.split(), capture_output=True)
            if p_compile.returncode:
                raise Exception('Compilation failed.')
        p_good = run(base_data_path / 'good', input=self.input, capture_output=True)
        if p_good.returncode:
            raise Exception('Execution of good file failed.')
        if p_good.stdout.rstrip() == self.output:
            return (True, 'OK')
        else:
            return (False, 'WRONG_ANSWER')

    @abstractmethod
    def check(self) -> tuple[bool, str]:
        return self.cpp_check()
