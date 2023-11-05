#!/usr/bin/env python3

import os
import random
import string
import argparse


def generate_random_string(length=18, use_numbers=True, use_specials=True):
    """ This function generates random strings based on arguments you've entered.

    Args:
        length (int, optional):
            The length of the string.
            Defaults to 18.
        use_numbers (bool, optional):
            Don't you need numbers in your string?
            Set this to False!
            Defaults to True.
        use_specials (bool, optional):
            Don't you need special characters in your string?
            Set this to False!
            Defaults to True.

    Returns:
        A random string.
        _type_: <class 'str'>
    """
    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_specials:
        chars += '!@#$%^&*()'

    random.seed(os.urandom(1024))
    return ''.join(random.choice(chars) for _ in range(length))


def CLI():
    parser = argparse.ArgumentParser(
        description='This script generates a secure and random string.\n You can use this string as your password or wherever you need a random string.'
    )

    # Positional arguments
    parser.add_argument(
        'length',
        type=int,
        nargs='?',
        default=18,
        help='Length of the random string',
    )
    # Optional arguments + -h which stands for help
    parser.add_argument(
        '-n', '--number',
        action='store_false',
        help='Exclude numbers in the random string',
    )
    parser.add_argument(
        '-s', '--special',
        action='store_false',
        help='Exclude special characters in the random string',
    )

    args = parser.parse_args()

    random_string = generate_random_string(
        args.length, args.number, args.special
    )
    print(random_string)
