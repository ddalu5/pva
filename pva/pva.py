#!/usr/bin/python
import argparse
from settings import *


def get_parser():
    parser = argparse.ArgumentParser(prog="Personal virtual assistant")
    # Project management arguments
    project_management = parser.add_argument_group('Project management')
    project_management.add_argument('-p', '--project', type=str, nargs=1,
                                    help="Unique project name")



if __name__ == "__main__":
    parser = get_parser()
    parser.print_help()
