#!/usr/bin/env python

import click
import os
import re
import sys
import csv

@click.command()
@click.argument('input_file', type = click.Path())
@click.argument('output_file', type = click.Path())
def main(input_file, output_file):    
    """
    Turn each line into a line of a CSV file
    """
    with open(output_file, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        line_no = 0
        with open(input_file, 'r') as latexfile:
            for latex_line in latexfile:
                line_no += 1
                spamwriter.writerow([line_no, latex_line])
    return None

if __name__ == '__main__':
    main()
