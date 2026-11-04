import contextlib
import io
from pathlib import Path
import runpy
import unittest
from unittest import mock


SCRIPT = Path(__file__).with_name("main.py")
ALPHABET = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!@$%&*")


def run_one_round(length, count):
    output = io.StringIO()
    with mock.patch("builtins.input", side_effect=[str(length), str(count), EOFError]), \
            contextlib.redirect_stdout(output):
        try:
            runpy.run_path(str(SCRIPT), run_name="__main__")
        except EOFError:
            pass  # The existing interactive loop asks for the next round.
    prefix = "Here is your password : "
    return [line[len(prefix):] for line in output.getvalue().splitlines()]


class PasswordGeneratorTests(unittest.TestCase):
    def test_does_not_use_the_seedable_random_generator(self):
        with mock.patch("random.choice", side_effect=AssertionError("insecure random source")):
            self.assertEqual(len(run_one_round(16, 1)[0]), 16)

    def test_preserves_requested_lengths_counts_and_alphabet(self):
        for length, count in [(12, 3), (1, 2), (24, 1), (8, 0)]:
            with self.subTest(length=length, count=count):
                passwords = run_one_round(length, count)
                self.assertEqual(len(passwords), count)
                for password in passwords:
                    self.assertEqual(len(password), length)
                    self.assertLessEqual(set(password), ALPHABET)


if __name__ == "__main__":
    unittest.main()
