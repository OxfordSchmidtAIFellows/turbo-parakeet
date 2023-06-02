import pandas as pd
import pytimeops

t = range(10)


def read_file(filename):

    df = pd.read_csv(filename)
    list_y = []
    for i, row in df.iterrows():
        V = df.iloc[i][5:].values
        MD = df.iloc[i][1:5].values
        list_y.append(pytimeops.Timeseries(t, V, MD))
    return list_y


list_1 = read_file('Fig1H-K_SI1G-I.csv')

print([ts.metadata for ts in list_1])
