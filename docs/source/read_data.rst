************
Read in data
************

.. currentmodule:: pytimeops.read_data

:func:`read_file<pytimeops.read_file>` is a function to read in a csv file and process it into a list of `Timeseries` objects.

Example::

    result = pytimeops.read_file('data.csv', 50, comments = "23/06/23 Honeybees", channel_title = "GRN")

Overview:

- :func:`read_file`

.. autofunction:: read_file

