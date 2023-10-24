from pathlib import Path

from src.stress_tester import StressTester

def main():
    st = StressTester()
    base_data_path = Path('data').resolve()
    (base_data_path / 'good').unlink()
    st.set_checker_file(base_data_path / 'default_checker.py')
    st.set_bad_file(base_data_path / 'bad.cpp')
    st.set_gen_file(base_data_path / 'generator.py')
    st.test()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program terminated.')
