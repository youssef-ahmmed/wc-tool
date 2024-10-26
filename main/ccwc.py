#!/usr/bin/env python3
import sys
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        description="Command-line tool that counts words, bytes, and lines for each file",
        prog="ccwc",
        epilog="Thanks for using %(prog)s! :)",
    )

    parser.add_argument("file", metavar="FILE", nargs="?", help="file to process")
    parser.add_argument("-c", "--bytes", action="store_true", help="print the byte counts")
    parser.add_argument("-l", "--lines", action="store_true", help="print the newline counts")
    parser.add_argument("-w", "--words", action="store_true", help="print the word counts")
    parser.add_argument("-m", "--chars", action="store_true", help="print the character counts")

    args = parser.parse_args()

    process_file(args)


def process_file(args):
    if args.file:
        content = read_file(args.file)
    else:
        content = sys.stdin.read()

    bytes_num = count_bytes(content)
    lines = count_lines(content)
    words = count_words(content)
    chars = count_chars(content)

    result = ""

    if args.bytes:
        result += f"{bytes_num}"
    elif args.lines:
        result += f"{lines}"
    elif args.words:
        result += f"{words}"
    elif args.chars:
        result += f"{chars}"
    else:
        result += f"  {lines}  {words} {bytes_num}"

    result += f" {args.file if args.file else ''}"

    print(result)


def count_bytes(text: str):
    return len(text.encode('utf-8'))


def count_lines(text: str):
    return len(text.splitlines())


def count_words(text: str):
    return len(text.split())


def count_chars(text: str):
    return len(text)


def read_file(file):
    try:
        with open(file, "rb") as f:
            binary_content = f.read()
            text = binary_content.decode('utf-8')

            return text
    except FileNotFoundError:
        sys.stderr.write(f"ccwc: {file}: No such file or directory\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
