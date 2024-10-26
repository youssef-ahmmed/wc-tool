# ccwc - Command-Line Word Count Tool

`ccwc` is a simple command-line tool for counting lines, words, bytes, and characters in text files or from standard input. It serves as an alternative to the Unix `wc` command, providing similar functionality with additional flexibility.

## Features

- Count lines, words, bytes, and characters in files or standard input.
- Easy to use with options for specific counts.
- Compatible with various operating systems.

## Installation

To install `ccwc`, you can clone this repository and install it using `pip`:

```bash
git clone https://github.com/youssef-ahmmed/wc-tool
cd ccwc
pip install .
```

## Usage

You can use `ccwc` directly from the command line. Here are some examples:

- To count lines in a file:
  ```bash
  ccwc -l path/to/file.txt
  ```

- To count words in a file:
  ```bash
  ccwc -w path/to/file.txt
  ```

- To count bytes in a file:
  ```bash
  ccwc -c path/to/file.txt
  ```

- To count characters in a file:
  ```bash
  ccwc -m path/to/file.txt
  ```

- To use `ccwc` without any options (counts lines, words, bytes, and characters):
  ```bash
  ccwc path/to/file.txt
  ```

- To read from standard input:
  ```bash
  cat path/to/file.txt | ccwc -l
  ```

## Running Tests

To run the tests for `ccwc`, you can use the following command:

```bash
python -m unittest discover -s tests
```

This will run all the test cases defined in the `tests` directory.

## Making it Global `ccwc`

To make `ccwc` available globally (so you can run it from any directory), ensure that the installation is done correctly. If you installed via pip as mentioned above, the executable should already be in your PATH. You can verify this by running:

```bash
ccwc --help
```

If you see the help message, the installation was successful!

## Project Structure

Here is a brief overview of the project structure:

```
.
├── main                     # Main source code directory
│   ├── ccwc.py              # The main script for the tool
│   └── __init__.py
├── pyproject.toml           # Build system configuration
├── README.md                # Project documentation
├── tests                    # Directory for test cases
│   ├── test_ccwc.py         # Test cases for the ccwc tool
└── test.txt                 # Sample text file for testing
```

## Contributing

If you would like to contribute to `ccwc`, feel free to submit a pull request or open an issue. All contributions are welcome!
