**********
Timeseries
**********

.. currentmodule:: pytimeops

:class:`Timeseries<pytimeops.Timeseries>` are callable objects that represent a time-series dataset.

Example::

    ts = pytimeops.Timeseries(time_indices = [1,2,3], values = [[10,100,105],[2,4,5]], metadata = {"sensillum": "s1", "sugar": "fruc"}, channels = ["GRN1","GRN2"], time_interval = 100)

Overview:

- :class:`Timeseries`

.. autoclass:: Timeseries

   .. method:: print()

   .. method:: rebin(new_tinterval)

   .. method:: compare_time_indices(timeseries)

   .. method:: compare_times(timeseries)

   .. method:: compare_values(timeseries)

   .. method:: compare_metadata(timeseries)

   .. method:: compare_channels(timeseries)

   .. method:: compare_time_interval(timeseries)

   .. method:: compare(timeseries)

   .. method:: is_empty(self)

   .. method:: get_metadata_attribute(attribute)

   .. method:: is_match(match_vars)

   .. method:: mean(self)

   .. method:: remove_channel(channel)

