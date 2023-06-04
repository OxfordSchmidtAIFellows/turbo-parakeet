import pandas as pd
import pytimeops


def read_file(filename):

    df = pd.read_csv(filename)
    t = range(10)
    list_y = []
    for i, row in df.iterrows():
        V = row[5:].values
        MD = dict(row[1:5])
        list_y.append(pytimeops.Timeseries(t, V, MD))
    return list_y


list_1 = read_file('Data/Fig1H-K_SI1G-I.csv')

print([ts.metadata for ts in list_1])
