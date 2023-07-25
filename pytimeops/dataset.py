import statistics
from copy import deepcopy

class Dataset:
    """Class to represent a dataset made of multiple Timeseries.

    Attributes:
        dataset (list(Timeseries)): list of the Timeseries datasets
        metadata (dict): global metadata about the dataset including
            e.g. time_interval [ms], filename and comments.

    """
    def __init__(self, dataset, metadata, times):
        """
        Parameters
        ----------

        dataset (list(Timeseries)): list of the Timeseries datasets

        metadata (dict): global metadata about the dataset including
            e.g. time_interval [ms], filename and comments.

        times (list(float)): list of the times for the Timeseries used [ms]

        """
        self.dataset = dataset
        self.metadata = metadata
        self.times = times

    def print(self, nrows=-1):
        """
        This function prints out the Dataset

        Args:
            nrows [int] max number of rows to print
        """
        print("Global Metadata: ", self.metadata)
        print("times [ms]: ", self.times)
        maxrows = len(self.dataset)
        if nrows != -1:
            maxrows = nrows
        for i in range(0, maxrows):
            print(i)
            self.dataset[i].print()

    def check_timeseries(self, timeseries):
        """
        Function to check if a timeseries is already in the dataset

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries present
        """
        for ts in self.dataset:
            if ts.compare(timeseries):
                return True
        return False

    def add_timeseries(self, Timeseries):
        """
        This function adds an extra timeseries to the dataset
        """
        if self.check_timeseries(Timeseries):
            print("Timeseries already in Dataset")
        else:
            self.dataset.append(Timeseries)

    def del_timeseries(self, Timeseries):
        """
        This function deletes a timeseries from the dataset
        """
        if not self.check_timeseries(Timeseries):
            print("Timeseries not in Dataset")
        else:
            self.dataset.remove(Timeseries)

    def rebin(self, new_tinterval):
        """
        Function to rebin the timeseries to be coarser

        Args:
            new_tinterval (float): new time interval / bin width [ms].
        """
        for ts in self.dataset:
            ts = ts.rebin(new_tinterval)
        self.metadata["time interval"] = new_tinterval
        self.times = self.dataset[0].times

    def clean(self, control_settings, remove_matches, verbose=False):
        """
        Function to remove any time series in the dataset coming from an
        experiment where the control test is all 0s.

        Args:
            control_settings [dict]: the metadata describing the experiment
                used as the control, where we want to test for all 0s.
                e.g. stim=sucr, conc=100
            remove_matches [dict]: the metadata for what matching data we want
                to remove if the control=0s, e.g. the same beeID & sensillum
            verbose [bool]: more verbose printouts
        """
        # Find the empty recordings in the control category
        empty_controls = []
        for ts in self.dataset:
            if (ts.is_match(control_settings) and ts.is_empty()):
                empty_controls.append(ts)
        # Clean the data of recordings matching the bad controls
        if verbose:
            print("These controls are empty: ")
            for ec in empty_controls:
                ec.print()
        for control in empty_controls:
            # find the values of the remove_matches metadata for our bad
            # control ts. i.e. what are the beeID and sensillum
            remove_vars = {}
            for var in remove_matches:
                remove_vars[var] = control.get_metadata_attribute(var)
            # find the other recordings for that beeID and sensillum, remove
            for ts in self.dataset:
                if (ts.is_match(remove_vars)):
                    if verbose:
                        print("Going to remove this timeseries: ")
                        ts.print()
                    self.del_timeseries(ts)

    def get_channels(self):
        """
        Function to return the list of channels

        Returns:
            list(str) of channels

        """
        return self.dataset[0].channels

    def list_types_in_metadata_attribute(self, attribute):
        """
        Function to return a list of the types present for a given metadata
        attribute, e.g. sugar types. Throws error if attribute not present.

        Args:
            attribute [str]: thing you want to know the types of.

        Return:
            list of types.
        """
        types = []
        for ts in self.dataset:
            md = ts.get_metadata_attribute(attribute)
            if md not in types:
                types.append(md)
        return types

    def mean_over_time(self):
        """
        Function to tell you the mean response for each channel in each
        timeseries in the dataset.

        Returns:
            list(list(float)) mean of timeseries channels for each timeseries
        """
        allmeans = []
        for ts in self.dataset:
            allmeans.append([statistics.mean(x) for x in ts.values])
        return allmeans

    def remove_channel(self, channel):
        """
        Function to remove reponses for a given channel in each timeseries.

        Args:
            channel [str]: the name of the channel to remove.
        """
        if channel in self.metadata['channels']:
            for ts in self.dataset:
                ts.remove_channel(channel)
            self.metadata['channels'].remove(channel)
        else:
            raise Exception("channel "+channel+" not in the dataset")

    def filter(self, allowed_mtd):
        """
        Function to remove timeseries if a particular combination of metadata
        isn't in a set of allowed values

        Args:
            allowed_mtd (dict[list]): metadata items to filter and their allowed
            values.

        Returns:
            dataset: with filter applied
        """
        new_data = []
        for ts in self.dataset:
            match = True
            for key,vals in allowed_mtd.items():
                if not ts.get_metadata_attribute(key) in vals:
                    match = False
            if match == True:
                new_data.append(ts)
        if len(new_data)==0:
            print("WARNING! no data matched the filter")
        new_dataset = deepcopy(self)
        new_dataset.dataset = new_data
        return new_dataset

    def mean(self, mtd_const):
        """
        Function to take the average at each time over timeseries with a
        varying metadata mtd_ave variable and the same mtd_const variables

        Args:
            mtd_const (dict[str]): metadata common to all the timeseries you
            want to average over

        Returns:
            Timeseries with the common metadata and the averaged timeseries
        """
        match_dataset = self.filter(mtd_const)
        time_indices = self.dataset[0].time_indices
        channels = self.metadata["channels"]
        means_allchannels = [ [] for c in range(0,len(channels)) ]
        for i,times in enumerate(time_indices):
            values = []
            for j in range(0,len(channels)):
                values.append([ match_dataset.dataset[k].values[j][i] for k in range(0,len(match_dataset.dataset)) ])
                means_allchannels[j].append(statistics.mean(values[j]))

        result = deepcopy(match_dataset.dataset[0])
        result.values = means_allchannels
        result.metadata = mtd_const

        return result
