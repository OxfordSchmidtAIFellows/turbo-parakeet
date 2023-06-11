import pandas as pd
import pytimeops as pto


def read_file(filename, Num_md, Num_b):
    """
    This function gets the .csv file, and returns lists of Timeseries objects

    Args:
        filename (str): input csv file path
        Num_md (int): number of types of metadata
        Num_b (int): number of bins
    Returns:
        list of Timeseries objects
    """

    df = pd.read_csv(filename)
    time_indices = range(Num_b)
    list_y = []
    for i, row in df.iterrows():
        values = row[Num_md+1:].values
        metadata = dict(row[1:Num_md+1])
        list_y.append(pto.Timeseries(time_indices, values, metadata))
    return list_y
