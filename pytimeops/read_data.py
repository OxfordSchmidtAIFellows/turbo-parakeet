import pandas as pd
import pytimeops as pto


def read_file(filename, time_interval, comments="", channel_title="GRN", nrows = -1):
    """
    This function gets the .csv file, and returns lists of Timeseries objects

    Args:
        filename (str): input csv file path.
        time_interval (float): width of each bin = time between measurements.
        comments (str): any comments about dataset to store as global metadata.
        channel_title (str): the column name that contains the measurement
            channels for each experiment. Defaults to the bee neurons "GRN".
    Returns:
        list of Timeseries objects
    """

    df = pd.read_csv(filename)
    totcolumns = len(df.columns)
    fname = filename.replace('.csv', '').replace('Data/', '')

    # set global metadata for dataset
    global_metadata = {}
    global_metadata['filename'] = fname
    global_metadata['comments'] = comments
    global_metadata['time interval'] = time_interval

    # list the different kinds of measurement channels in the dataset
    global_metadata['channels'] = df[channel_title].unique().tolist()
    num_channels = df[channel_title].nunique()  # count the number of channels

    # find columns containing experiment metadata (before the channels one)
    channel_index = df.columns.get_loc(channel_title)
    finalmd_index = channel_index-1

    # then set the time indices from the remaining columns
    numtimes = totcolumns - channel_index - 1
    time_indices = list(map(int, range(numtimes)))
    timeseries_list = []

    values_allchannels = []
    for i, row in df.iterrows():
        if nrows>0 and not i<(nrows*num_channels): continue
        values = list(map(int, row[channel_index+1:].values))
        values_allchannels.append(values)
        metadata = dict(row[0:finalmd_index+1])
        if (i+1) % num_channels == 0:
            timeseries_list.append(
                pto.Timeseries(
                    time_indices,
                    values_allchannels,
                    metadata,
                    global_metadata['channels'].copy(),
                    float(time_interval)
                )
            )
            values_allchannels = []

    times = [index*float(time_interval) for index in time_indices]
    dataseries = pto.Dataset(timeseries_list, global_metadata, times)

    return dataseries
