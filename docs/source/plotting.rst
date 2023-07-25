************
Plot the data
************

.. currentmodule:: pytimeops.plotting

:func:`plot_firing_rates<pytimeops.plotFiringRates>` is a function to plot firing rates for a set of data series, each averaged in some way. 

Example::

    result = pytimeops.read_file('data.csv', 50, comments = "23/06/23 Honeybees", channel_title = "GRN")
    pytimeops.plot_firing_rates(dataset, "Fruc", ["0mM", "100mM"], {"Fruc": {"0mM": <timeseries of means>, "100mM": <timeseries of means>}}, "/my/folder/", colmap="tab20", padcoords=[0.08,0.08], padsize=[0.90,0.86]):

Overview:

- :func:`plot_firing_rates`

.. autofunction:: plot_firing_rates

