# Password-Generator
Create a password generator with a few lines of python code!

Run `python main.py` with Python 3.6 or newer, then enter the length and number
of passwords to generate. Press Ctrl+C to leave the interactive loop.

Password characters are selected with Python's `secrets` module, which uses the
operating system's secure randomness source. The default `random` generator is
intended for simulation and should not be used for passwords.

Run the standard-library regression tests with `python -m unittest -v`.
