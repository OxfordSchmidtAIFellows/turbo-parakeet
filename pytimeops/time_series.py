import statistics


class Timeseries:
    """Class to represent Timeseries data

    Attributes:
        time_indices (list(int)): time indices for each data point.
        times (list(float)): times for each data point [ms].
        values (list(list(int))):  response data for each time and channel.
        metadata (dict): metadata, other dataset attributes.
        channels (list(str)): names of each measurement channel: neurons here
        time_interval (float): binwidth / time between measurements [ms]

    """
    def __init__(self, time_indices, values, metadata, channels,
                 time_interval):
        """
        Parameters
        ----------

        time_indices (list(int)): time indices (in this case bins)

        values (list(list(int))): Values of each sample at each time
            (in this case [GRN1,GRN2,GRN3])

        metadata (dictionary):
            Other attributes of the dataset which
            can be numerical or non-numerical
            (e.g.: sensillum (non-numerical),
            sugar(non-numerical), Concentration (numerical))

        channels (list(str)): names of each measurement channel (e.g. neurons)

        time_interval (float): binwidth = time between measurements [ms]

        """
        self.time_indices = time_indices
        self.times = [index*time_interval for index in time_indices]
        self.values = values
        self.metadata = metadata
        self.channels = channels
        self.time_interval = time_interval

    def print(self):
        """
        Function to print out the Timeseries
        """
        print("Metadata: ", self.metadata)
        print("Time interval [ms]: ", self.time_interval)
        print("t indices: ", self.time_indices)
        print("t [ms]: ", self.times)
        for i in range(0, len(self.channels)):
            print(self.channels[i], " : ", self.values[i])

    def rebin(self, new_tinterval):
        """
        Function to rebin the time series to be coarser.

        Args:
             new_tinterval (float): new time interval / bin width [ms].
        """
        # First check if the new width is an integer multiple of the old one
        if ((new_tinterval % self.time_interval != 0) or
                (self.time_interval*len(self.times) % new_tinterval != 0)):
            raise Exception("Sorry, the new binning won't work, "
                            "pick an int. multiple of ",
                            self.time_interval,
                            " and a divider of ",
                            self.time_interval*len(self.times))

        # Find the Scale Factor for how much fatter the new bins are
        sf = int(new_tinterval/self.time_interval)

        # Loop over current bins to rebin, keep 'time' as low edge
        new_times = []
        num_values = len(self.values)
        new_values = []
        for i in range(0, num_values):
            new_values.append([])
        tmp_value = [0]*num_values
        for i in range(0, len(self.times)):
            for j in range(0, num_values):
                tmp_value[j] += self.values[j][i]
            if ((i+1) % sf) == 0:
                new_times.append(self.times[i+1-sf])
                for j in range(0, num_values):
                    new_values[j].append(tmp_value[j])
                    tmp_value[j] = 0
        new_time_indices = list(range(len(new_times)))

        # put into Timeinterval
        self.times = new_times
        self.time_indices = new_time_indices
        self.time_interval = new_tinterval
        self.values = new_values

    def compare_time_indices(self, timeseries):
        """
        Function to compare if two timeseries have the same time_indices

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        return all(x == y for x, y in
                   zip(timeseries.time_indices, self.time_indices))

    def compare_times(self, timeseries):
        """
        Function to compare if two timeseries have the same times

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        return all(x == y for x, y in zip(timeseries.times, self.times))

    def compare_values(self, timeseries):
        """
        Function to compare if two timeseries have the same values

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        for ts, s in zip(timeseries.values, self.values):
            if not all(x == y for x, y in zip(ts, s)):
                return False
        return True

    def compare_metadata(self, timeseries):
        """
        Function to compare if two timeseries have the same metadata

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        return timeseries.metadata == self.metadata

    def compare_channels(self, timeseries):
        """
        Function to compare if two timeseries have the same channels

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        return all(x == y for x, y in zip(timeseries.channels, self.channels))

    def compare_time_interval(self, timeseries):
        """
        Function to compare if two timeseries have the same time interval

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        return timeseries.time_interval == self.time_interval

    def compare(self, timeseries):
        """
        Function to compare if two timeseries are the same

        Args:
             timeseries (Timeseries): timeseries to check.

        Returns:
             bool: is timeseries the same
        """
        return all([self.compare_time_indices(timeseries),
                    self.compare_times(timeseries),
                    self.compare_values(timeseries),
                    self.compare_metadata(timeseries),
                    self.compare_channels(timeseries),
                    self.compare_time_interval(timeseries)])

    def is_empty(self):
        """
        Function to check if a timeseries is empty.
        Defined here as all channels are 0 for all times.

        Returns:
             bool: is timeseries bad
        """
        for response in self.values:
            channelbad = all(x == 0 for x in response)
            if not channelbad:
                return False
        return True

    def get_metadata_attribute(self, attribute):
        """
        Function to return the value of a metadata attribute if it exists

        Args:
            attribute [str]: the metadata attribute we want to lookup

        Returns:
            something: value of the metadata

        """
        md = None
        try:
            md = self.metadata[attribute]
        except KeyError:
            print("The metadata isn't present in the timeseries!")
        return md

    def is_match(self, match_vars):
        """
        Function to tell you if a timeseries matches a set of metadata reqs.

        Args:
            match_vars [dict]: the metadata attribute we want to check
                and the values we want them to have.

        Returns:
            bool: does it match?

        """
        for setting, value in match_vars.items():
            if self.get_metadata_attribute(setting) != value:
                return False
        return True

    def mean(self):
        """
        Function to tell you the mean response for each channel in timeseries.

        Returns:
            list(float) mean of timeseries channels
        """
        means = [statistics.mean(x) for x in self.values]
        return means

    def remove_channel(self, channel):
        """
        Function to remove reponses for a given channel.

        Args:
            channel [str]: the name of the channel to remove.
        """
        try:
            index = self.channels.index(channel)
        except KeyError:
            print("The channel isn't present in the timeseries!")
        self.channels.pop(index)
        self.values.pop(index)
