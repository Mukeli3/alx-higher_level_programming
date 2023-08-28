#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        # sys.exc_info() returns a tuple with 3 values
        # 0 - exception being handled type
        # 1 - args passed to exception class constructor
        # 2 - stack info, traceback
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return False
