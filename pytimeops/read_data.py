import pandas as pd
import pytimeops as pto
import sys

def read_file(filename, Num_md, Num_b):
    """
    This function gets the .csv file, and returns lists of Timeseries objects.
    """

    df = pd.read_csv(filename)
    t = range(Num_b)
    list_y = []
    for i, row in df.iterrows():
        V = row[Num_md+1:].values
        MD = dict(row[1:Num_md+1])
        list_y.append(pto.Timeseries(t, V, MD))
    return list_y


def main(inputCSV, verbose=False):
    """
    This main function takes the csv file input from the command line and reads it into the Timeseries, with additional debugging printouts if verbose=True.
    """
    # read in csv file to Timeseries format
    list_1 = read_file(inputCSV, 4, 10)

    if verbose:
        print([ts.metadata for ts in list_1])
        print([ts.values for ts in list_1])

if __name__ == "__main__":
    """
    example usage:
    $ python pytimeops/read_data.py -i Data/Fig1H-K_SI1G-I.csv -v
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Turn on verbose messages", action="store_true", default=False)
    parser.add_argument("-i", "--inputCSV", help="Path to csv file to read in", default=None)
 
    args = parser.parse_args()
    verbose = args.verbose
    inputfile = args.inputCSV

    # check input file is sensible
    if not inputfile:
        sys.exit("FATAL: not giving an input file, add an '-i' argument")
    elif ".csv" not in inputfile:
        sys.exit("FATAL: not giving a csv formatted input file")

    main(inputfile, verbose=verbose)

