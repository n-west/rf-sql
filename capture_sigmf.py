
#import pysdruhd
import numpy as np

import argparse

# we want to make a usrp object based on given parameters, then start recording
# and save a sigmf file


def setup_parser():
    """
    Create all the args
    """
    parser = argparse.ArgumentParser(description="A USRP recorder utility with SigMF support")
    parser.add_argument('filename')
    parser.add_argument('freq')
    parser.add_argument('rate')
    parser.add_argument('gain')
    parser.add_argument('num_samples')
    parser.add_argument('start_time')
    return parser


def main():
    """
    self evident
    """
    args = setup_parser().parse_args()

    # create usrp

if __name__ == '__main__':
    main()
