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

    def print(self):
        """
        This function prints out the Dataset
        """
        print("Global Metadata: ", self.metadata)
        for i in range(0, len(self.dataset)):
            print(i, self.dataset[i])

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
        if self.checkTimeseries(Timeseries):
            print("Timeseries already in Dataset")
        else:
            self.dataset.append(Timeseries)

    def del_timeseries(self, Timeseries):
        """
        This function deletes a timeseries from the dataset
        """
        if not self.checkTimeseries(Timeseries):
            print("Timeseries not in Dataset")
        else:
            self.dataset.remove(Timeseries)
