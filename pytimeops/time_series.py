class Timeseries:
    """Class to represent Timeseries data

    Attributes:
        time_indices (list(int)): times for each data point.
        values (list(list(int))): sensilla valies for each time.
        metadata (dict): metadata, other dataset attributes.

    """
    def __init__(self, time_indices, values, metadata):
        """
        Parameters
        ----------

        time_indices (list(int)): time samples (in this case bins)

        values (list(list(int))): Values of each sample at each time
            (in this case [GRN1,GRN2,GRN3])

        metadata (dictionary):
            Other attributes of the dataset which
            can be numerical or non-numerical
            (in this case: sensillum (non-numerical),
            sugar(non-numerical), Concentration (numerical))

        """
        self.time_indices = time_indices
        self.values = values
        self.metadata = metadata
