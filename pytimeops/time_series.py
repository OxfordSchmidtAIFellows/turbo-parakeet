class Timeseries:
    def __init__(self, t, v, md):
        """
        Parameters
        ----------

        time_index (t): list of int
            time samples (in this case bins)

        values (v): list of int
            Values of each sample (in this case [GRN1,GRN2,GRN3])

        metadata (md): dictionary
            Other attributes of the dataset which
            can be numerical or non-numerical
            (in this case: sensillum (non-numerical),
            sugar(non-numerical), Concentration (numerical))

        """
        self.time_index = t
        self.values = v
        self.metadata = md
