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
        The function prints out the Dataset
        """
        print("Global Metadata: ", self.metadata)
        for i in range(0, len(self.dataset)):
            print(i, self.dataset[i])
