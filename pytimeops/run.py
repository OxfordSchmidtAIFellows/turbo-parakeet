# import pandas as pd
import pytimeops as pto
import sys

# define command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Turn on verbose messages",
                    action="store_true", default=False)
parser.add_argument("-i", "--inputCSV", help="Path to csv file to read in",
                    default=None)
parser.add_argument("-c", "--comments", help="Comments on dataset to add to metadata",
                    default="")
parser.add_argument("-t", "--time_interval", help="[ms] time interval between measurements, default binwidth",
                    default=None)



def main(inputCSV, time_interval, comments, verbose=False):
    """
    This main function performs the workflow:
    1. takes the csv file input from the command line
       and reads it into the Timeseries,
    2. ...

    Args:
        inputCSV (str): of full path to .csv input file
        verbose (bool): Additional debugging printouts if True
        time_interval (float): width of each bin = time between measurements
        comments (str): any comments about dataset to store as global metadata
    Returns:
        void
    """
    # Step 1: read in csv file toi Dataset of Timeseries format
    dataset = pto.read_file(inputCSV, 4, 10, time_interval, comments)

    if verbose:
        dataset.print()
        for ts in dataset.dataset: ts.print()

    # Step 2....


if __name__ == "__main__":
    """
    example usage:
    $ python pytimeops/run.py -i Data/Fig1H-K_SI1G-I.csv -v
    """
    args = parser.parse_args()
    verbose = args.verbose
    inputfile = args.inputCSV
    comments = args.comments
    time_interval = args.time_interval

    # check input file is sensible
    if not inputfile:
        sys.exit("FATAL: not giving an input file, add an '-i' argument")
    elif ".csv" not in inputfile:
        sys.exit("FATAL: not giving a csv formatted input file")
    elif not time_interval:
        sys.exit("FATAL: not giving a time interval for the measurements, add a -t argument in [ms]")

    main(inputfile, time_interval, comments, verbose=verbose)
