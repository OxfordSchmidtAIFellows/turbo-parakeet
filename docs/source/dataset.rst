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

   .. method:: print(nrows=-1)

   .. method:: check_timeseries(timeseries)

   .. method:: add_timeseries(Timeseries)

   .. method:: del_timeseries(Timeseries)

   .. method:: rebin(new_tinterval)

   .. method:: clean(control_settings, remove_matches, verbose=False)

   .. method:: get_channels(self)

   .. method:: list_types_in_metadata_attribute(attribute)

   .. method:: mean(self)

   .. method:: remove_channel(channel)

   .. method:: filter(key, allowed_values)

