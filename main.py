#!/usr/bin/env python3

import os, argparse

SAVEPATH = os.path.expanduser("~/.py-cli")

parser = argparse.ArgumentParser(description="py cli template")
parser.add_argument("-i", "--input", help="cmd with some input", action="store")
parser.add_argument(
    "-b", "--boolean", help="cmd with boolean true", action="store_true"
)


def run():
    args = parser.parse_args()

    if args.input:
        input = args.input
        print(input)
        # Something
    elif args.boolean:
        print("boolean true!")
    else:
        # Do something
        parser.print_help()


run()
