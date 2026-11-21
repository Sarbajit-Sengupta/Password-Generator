import subprocess
import sys
import unittest
from pathlib import Path


class CliTests(unittest.TestCase):
    def test_invalid_input_recovers_and_eof_exits(self):
        result = subprocess.run([sys.executable, str(Path(__file__).with_name('main.py'))],
                                input='oops\n-2\n0\n4\n2\n', text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.split('Here is your password : ')[1:]
        self.assertEqual(len(lines), 2)
        self.assertTrue(all(len(line.splitlines()[0]) == 4 for line in lines))
        self.assertEqual(result.stdout.count('Enter positive whole numbers'), 3)


if __name__ == '__main__':
    unittest.main()
