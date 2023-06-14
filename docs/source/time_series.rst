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
