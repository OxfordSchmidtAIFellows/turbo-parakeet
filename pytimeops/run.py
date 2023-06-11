#import pandas as pd
import pytimeops as pto
import sys

# define command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Turn on verbose messages",
                    action="store_true", default=False)
parser.add_argument("-i", "--inputCSV", help="Path to csv file to read in",
                    default=None)


def main(inputCSV, verbose=False):
    """
    This main function performs the workflow:
    1. takes the csv file input from the command line
       and reads it into the Timeseries,
    2. ...

    Args:
        inputCSV (str): of full path to .csv input file
        verbose (bool): Additional debugging printouts if True
    Returns:
        void
    """
    # Step 1: read in csv file to Timeseries format
    list_1 = pto.read_file(inputCSV, 4, 10)

    if verbose:
        print([ts.metadata for ts in list_1])
        print([ts.values for ts in list_1])

    # Step 2....


if __name__ == "__main__":
    """
    example usage:
    $ python pytimeops/run.py -i Data/Fig1H-K_SI1G-I.csv -v
    """
    args = parser.parse_args()
    verbose = args.verbose
    inputfile = args.inputCSV

    # check input file is sensible
    if not inputfile:
        sys.exit("FATAL: not giving an input file, add an '-i' argument")
    elif ".csv" not in inputfile:
        sys.exit("FATAL: not giving a csv formatted input file")

    main(inputfile, verbose=verbose)
