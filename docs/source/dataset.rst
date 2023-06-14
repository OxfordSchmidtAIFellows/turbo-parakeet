**********
Dataset
**********

.. currentmodule:: pytimeops

:class:`Dataset<pytimeops.Dataset>` are callable objects that represent a collection of time series datasets.

Example::

  ts = pytimeops.Timeseries(...)
  ds = pytimeops.Dataset(ts, metadata = {"time interval [ms]": 100, "comments": "data associated with Figure 1H-K from the 2022 iScience paper", "filename": "mydata.csv"})

Overview:

- :class:`Dataset`

.. autoclass:: Dataset

   .. method:: print()