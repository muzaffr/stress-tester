from pathlib import Path
from subprocess import run, TimeoutExpired


class StressTester:

    def __init__(self):

        self._checker_file: None | Path = None
        self._bad_file:     None | Path = None
        self._gen_file:     None | Path = None

    def set_checker_file(self, path: Path) -> None:
        '''Set the checker file path.'''
        self._checker_file = path

    def set_bad_file(self, path: Path) -> None:
        '''Set the bad (target) file path.'''
        if path.suffix == '.cpp':
            p_bad = run(f'g++ {path} -o {path.parent / "bad"}'.split(), capture_output=True)
            if p_bad.returncode:
                raise RuntimeError(f'Compilation of bad file failed:\n{p_bad.stderr.decode()}')
            self._bad_file = path.parent / 'bad'
        else:
            self._bad_file = path

    def set_gen_file(self, path: Path) -> None:
        '''Set the random test case generator file path.'''
        self._gen_file = path

    def _run_test(self, test_number: int) -> int:
        '''Run one test.'''
        p_gen = run(str(self._gen_file), capture_output=True)
        if p_gen.returncode:
            raise Exception(f'Execution of generator file failed.\n{p_gen.stderr.decode()}')
        test_input = p_gen.stdout
        print(
            f'\nTest #{test_number}\n'
            f'Input:\n'
            f'{test_input.decode().rstrip()}'
        )
        verdict, message = '', ''
        try:
            p_bad = run(str(self._bad_file), input=test_input, capture_output=True, timeout=3)
            if p_bad.returncode:
                message += f'bad file exited with return code {p_bad.returncode}'
                message += p_bad.stderr.decode().rstrip()
            print(f'Output:\n{p_bad.stdout.decode().rstrip()}')
            checker_input = test_input + bytes([0x1C]) + p_bad.stdout
            p_checker = run(str(self._checker_file), input=checker_input, capture_output=True)
            if p_checker.returncode:
                message += f'checker file exited with return code {p_bad.returncode}'
                message += p_checker.stderr.decode().rstrip()
            verdict = p_checker.stdout.decode().rstrip()
        except TimeoutExpired:
            verdict = 'TIME_LIMIT_EXCEEDED'
        print(f'Verdict: {verdict}')
        if message:
            print(f'Message:\n{message}')
        if verdict != 'OK':
            return 1
        return 0

    def test(self, iterations: int = 10000) -> None:
        '''Run stress test.'''
        for iteration in range(iterations):
            if self._run_test(iteration + 1):
                break
