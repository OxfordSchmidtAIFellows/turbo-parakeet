import pandas as pd
import pytimeops as pto


def read_file(filename, Num_md, Num_b):
    """
    This function gets the .csv file, and returns lists of Timeseries objects.
    """

    df = pd.read_csv(filename)
    t = range(Num_b)
    list_y = []
    for i, row in df.iterrows():
        V = row[Num_md+1:].values
        MD = dict(row[1:Num_md+1])
        list_y.append(pto.Timeseries(t, V, MD))
    return list_y


list_1 = read_file('Data/Fig1H-K_SI1G-I.csv', 4, 10)

'#print([ts.metadata for ts in list_1])'
'#print([ts.values for ts in list_1])'
'#print(hasattr(pytimeops, read_file))'
