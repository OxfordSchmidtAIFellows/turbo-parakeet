# import pandas as pd
import pytimeops as pto
import sys
from copy import deepcopy

# define command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",
                    help="verbose output", action="store_true", default=False)
parser.add_argument("-i", "--inputCSV",
                    help="Path to csv file to read in", default=None)
parser.add_argument("-c", "--comments",
                    help="Comments on dataset for metadata", default="")
parser.add_argument("-t", "--time_interval",
                    help="[ms] time interval / binwidth", default=None)


def main(inputCSV, time_interval, comments, verbose=False):
    """
    This main function performs the workflow:
    1. takes the csv file input from the command line
       and reads it into the dataset/Timeseries format.
       print out some properties to sanity check
    2. cleans bad recordings / removes un-needed channels
    3. produces some versions with different binning

    Args:
        inputCSV (str): of full path to .csv input file
        verbose (bool): Additional debugging printouts if True
        time_interval (float): width of each bin = time between measurements
        comments (str): any comments about dataset to store as global metadata
    Returns:
        void
    """
    # Step 1: read in csv file toi Dataset of Timeseries format
    print("Step 1")
    dataset = pto.read_file(inputCSV, time_interval, comments)

    if verbose:
        print("verbose! printing the dataset:")
        dataset.print()
        for ts in dataset.dataset:
            ts.print()

    # print out some properties of the dataset
    beeIDs = dataset.list_types_in_metadata_attribute("BeeID")
    print("how many bees? ", len(beeIDs), ". With these names: ", beeIDs)
    sensilla = dataset.list_types_in_metadata_attribute("sensillum")
    print("how many sensilla? ", len(sensilla),
          ". With these names: ", sensilla)
    sugars = dataset.list_types_in_metadata_attribute("sugar")
    print("how many sugars? ", len(sugars), ". With these names: ", sugars)
    concentrations = dataset.list_types_in_metadata_attribute("concentration")
    print("how many concentrations? ", len(concentrations),
          ". With these names: ", concentrations)
    channels = dataset.get_channels()
    print("how many channels? ", len(channels),
          ". With these names: ", channels)
#    means = dataset.mean_over_time()
#    print("what are the means of the dataset?", means)

    # Step 2. Clean bad recordings
    print("Step 2")
    dataset.clean({"sugar": "sucr", "concentration": "100mM"},
                  ["BeeID", "sensillum"], verbose=verbose)
    # remove the GRN3
    dataset.remove_channel("GRN3")

    # Step 3. Produce some new datasets with different binnings
    # (assuming 20ms file to start with for now)
    print("Step 3")
    dataset_40ms = deepcopy(dataset)
    dataset_40ms.rebin(40)
    if verbose:
        print("verbose! printing the dataset:")
        dataset_40ms.print()
    #    dataset.print()

    # Now lets look at the fructose data, and find the average responses over
    # beeID/sensillum at each concentration
    # store these in a dict of dicts for sugars and each conc for each sugar
    outplotdir = "plots/"
    means = {}
    means_40ms = {}
    for sugar in sugars:
        means[sugar] = {}
        means_40ms[sugar] = {}
        for conc in concentrations:
            # return a Timeseries object with this const. metadata and the
            # means for each time.
            means[sugar][conc] = dataset.mean({"sugar": sugar,
                                              "concentration": conc})
            means_40ms[sugar][conc] = dataset_40ms.mean({"sugar": sugar,
                                                        "concentration": conc})
            if verbose:
                means[sugar][conc].print()

        pto.plot_firing_rates(dataset, sugar, concentrations,
                              means, outplotdir)
        pto.plot_firing_rates(dataset_40ms, sugar, concentrations,
                              means_40ms, outplotdir)


if __name__ == "__main__":
    """
    example usage:
    $ python pytimeops/run.py -i Data/Fig1H-K_SI1G-I.csv -t 20 -v
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
        sys.exit("FATAL: not giving a time interval, add a -t argument [ms]")

    main(inputfile, time_interval, comments, verbose=verbose)
