import subprocess
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from main.ccwc import main


class TestCCWCCommand(unittest.TestCase):
    test_file = "../test.txt"

    def run_wc_test_file(self, option=None):
        wc_command = ["wc"] + ([option, self.test_file] if option else [self.test_file])
        wc_output = subprocess.check_output(wc_command).decode().strip()

        sys.argv = ["ccwc"] + ([option, self.test_file] if option else [self.test_file])
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            ccwc_output = mock_stdout.getvalue().strip()

        self.assertEqual(ccwc_output, wc_output)

    def run_wc_test_stdin(self, option=None):
        with open(self.test_file, "r") as f:
            file_content = f.read()

        input_data = file_content.encode()
        wc_output = subprocess.check_output(["wc"] + ([option] if option else []), input=input_data).decode().strip()

        with patch("sys.stdin", new=StringIO(file_content)):
            sys.argv = ["ccwc"] + ([option] if option else [])
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                main()
                ccwc_output = mock_stdout.getvalue().strip()

        self.assertEqual(ccwc_output, wc_output)

    def test_count_no_options(self):
        self.run_wc_test_file()

    def test_count_stdin(self):
        self.run_wc_test_stdin()

    def test_line_count(self):
        self.run_wc_test_file("-l")

    def test_line_count_stdin(self):
        self.run_wc_test_stdin("-l")

    def test_bytes_count(self):
        self.run_wc_test_file("-c")

    def test_bytes_count_stdin(self):
        self.run_wc_test_stdin("-c")

    def test_words_count(self):
        self.run_wc_test_file("-w")

    def test_words_count_stdin(self):
        self.run_wc_test_stdin("-w")

    def test_chars_count(self):
        self.run_wc_test_file("-m")

    def test_chars_count_stdin(self):
        self.run_wc_test_stdin("-m")


if __name__ == "__main__":
    unittest.main()
