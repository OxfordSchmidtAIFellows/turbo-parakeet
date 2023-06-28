import pandas as pd
from collections import defaultdict
import numpy as np
import pytimeops as pto


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

    def rebin(self, new_tinterval):
        """
        Function to rebin the time series to be coarser.

        Args:
             new_tinterval (float): new time interval / bin width [ms].
        """
        for ts in self.dataset:
            ts.rebin(new_tinterval)
        self.metadata["time interval"] = new_tinterval

    def cluster_each_group(self, features, method, grn_idx):
        """
        This function gets the dataset and the feature that you want
        to group based on that, applies clustering on each group
        and returns centroids of clusters.
        """

        # Initialize an empty DataFrame to store the centroids
        centroids_df = pd.DataFrame(columns=['group', 'Number', 'centroid'])

        # df_selected_columns = df.iloc[:, [feature] + list(range(5, 15))]
        # grouped = df_selected_columns.groupby(df_selected_columns.columns[0])

        grouped = defaultdict(list)
        for ts in self.dataset:
            ts_feature = "_".join([ts.metadata[feat] for feat in features])
            grouped[ts_feature].append(ts)

        for group_name, group_list in grouped.items():
            #print(f"Processing group: {group_name}")
            group_data = [ts.values[grn_idx] for ts in group_list]
            group_data = np.asarray(group_data)

            # Apply K-means clustering
            result = pto.apply_clustering(group_data, 15, method)
            # Create a new DataFrame to store the group name and centroid
            group_centroids_df = pd.DataFrame({'group': [group_name],
                                               'Number': [result[0]],
                                               'centroid': [result[1:]]})
            centroids_df = pd.concat([centroids_df, group_centroids_df])
            # Append the group centroids to the main centroids DataFrame
            # group_centroids = pto.apply_clustering(group_data.iloc[:, -5:].values,
                                                     3)
            # print(group_centroids)
            # group_centroids = 10
        return centroids_df

    def filter(self, key, allowed_values):
        """
        Parameters
        ----------
        key
            key for the time series metadata
        allowed_values : list
            Allowed values for that key
        """
        new_dataset = []
        for i, ts in enumerate(self.dataset):
            if ts.metadata[key] in allowed_values:
                new_dataset.append(ts)
        self.dataset = new_dataset
