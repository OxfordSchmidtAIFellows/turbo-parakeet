class Timeseries:
    """Class to represent Timeseries data

    Attributes:
        time_indices (list(int)): time indices for each data point.
        times (list(float)): times for each data point [ms].
        values (list(list(int))): sensilla valies for each time.
        metadata (dict): metadata, other dataset attributes.
        channels (list(str)): names of each measurement channel: in this case neurons
        time_interval (float): width of each bin = time between measurements [ms]

    """
    def __init__(self, time_indices, values, metadata, channels, time_interval):
        """
        Parameters
        ----------

        time_indices (list(int)): time indices (in this case bins)

        values (list(list(int))): Values of each sample at each time
            (in this case [GRN1,GRN2,GRN3])

        metadata (dictionary):
            Other attributes of the dataset which
            can be numerical or non-numerical
            (in this case: sensillum (non-numerical),
            sugar(non-numerical), Concentration (numerical))

        channels (list(str)): names of each measurement channel: in this case neurons

        time_interval (float): width of each bin = time between measurements [ms]

        """
        self.time_indices = time_indices
        self.times = [ index*time_interval for index in time_indices ]
        self.values = values
        self.metadata = metadata
        self.channels = channels
        self.time_interval = time_interval


    def print(self):
        """
        The function prints out the Timeseries
        """
        print("Metadata: ",self.metadata)
        print("Time interval [ms]: ", self.time_interval)
        print("t index, t [ms], ", self.channels)
        for i in range(0,len(self.time_indices)):
            print(self.time_indices[i], self.times[i], [ self.values[j][i] for j in range(0,len(self.values)) ])
