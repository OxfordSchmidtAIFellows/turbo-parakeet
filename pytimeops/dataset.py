import statistics

class Dataset:
    """Class to represent a dataset made of multiple Timeseries.

    Attributes:
        dataset (list(Timeseries)): list of the Timeseries datasets
        metadata (dict): global metadata about the dataset including
            e.g. time_interval [ms], filename and comments.

    """
    def __init__(self, dataset, metadata):
        """
        Parameters
        ----------

        dataset (list(Timeseries)): list of the Timeseries datasets

        metadata (dict): global metadata about the dataset including
            e.g. time_interval [ms], filename and comments.

        """
        self.dataset = dataset
        self.metadata = metadata

    def print(self, nrows=-1):
        """
        This function prints out the Dataset

        Args:
            nrows [int] max number of rows to print
        """
        print("Global Metadata: ", self.metadata)
        maxrows = len(self.dataset)
        if nrows != -1: maxrows = nrows
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

    def clean(self, control_settings, remove_matches, verbose=False):
        """
        Function to remove any time series in the dataset coming from an
        experiment where the control test is all 0s.

        Args:
            control_settings [dict]: the metadata describing the experiment
                used as the control, where we want to test for all 0s.
                e.g. stim=sucr, conc=100
            remove_matches [dict]: the metadata for what matching data we want
                to remove if the control is zero, e.g. the same beeID and sensillum
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
            for ec in empty_controls: ec.print()
        for control in empty_controls:
            # find the values of the remove_matches metadata for our bad control ts
            # i.e. what are the beeID and sensillum
            remove_vars = {}
            for match_var in remove_matches:
                remove_vars[match_var] = control.get_metadata_attribute(match_var)
            # find the other recordings for that beeID and sensillum and remove them
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
            if not md in types: types.append(md)
        return types

    def mean(self):
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
