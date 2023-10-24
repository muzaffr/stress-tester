# Stress Tester
A simple tool to stress test competitive programming solutions (or anything really).

## How it works
In each iteration, the generator file is run to generate a random test case. This is passed as input to the bad (target/interesting/suspicious) file, and the test case and the output of the bad file are passed to the checker file. If there is a single valid output, then the checker file can use a "good" file to directly compare the outputs. If there are several possible valid outputs, the checker is used to judge the output.

## How to use
In `main.py`, set the appropriate file paths and run it. Sample good, bad and checker files have been included.

## Supported languages
C++ is supported. Python and any scripting languages can be used with a shebang and executable permissions.

## Supported operating systems
Linux. Might work with Windows.
