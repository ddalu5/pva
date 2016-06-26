#!/usr/bin/python
import argparse
from settings import *


def get_parser():
    parser = argparse.ArgumentParser(prog="Personal virtual assistant")
    # Project management arguments
    project_management = parser.add_argument_group('Project management')
    project_management.add_argument('-p', '--project', type=str, nargs=1,
                                    help="Project's unique name", required=False)
    project_management.add_argument('-d', '--domaine-names', type=str, nargs='+',
                                    help="Domaines names list",
                                    required=False)
    project_management.add_argument('-isd', '--ignored-subdomaines', type=str,
                                    nargs='+', help="Subdomaines to be ignored",
                                    required=False)
    project_management.add_argument
    return parser



if __name__ == "__main__":
    parser = get_parser()
    parser.print_help()
