import matplotlib
import matplotlib.pyplot as plt


def plot_firing_rates(dataset, constvar, comparevar, means, outplotdir,
                      colmap="tab20", padcoords=[0.08, 0.08], padsize=[0.90, 0.86]):
    '''
    Function to plot firing rates for a set of data series, each averaged
    in some way. All the channels are plotted. E.g for a constvar=Fruc,
    comparevar = list of concentrations, 1 plot of fructose is made showing
    the firing rates for all the concentrations and all the GRNs in dataset.

    Args:
        dataset (Dataset): dataset object to get the metadata, channels etc.
        constvar (str): variable you want to have constant for the plot.
        comparevar (list(str)): list of dataseries you want to put on 1 plot.
        means (dict(dict(Timeseries))): 1st index is for constvar, 2nd index
            is comparevar - each dataseries on the plot. contents is the mean
            responses at each time.
        outplotdir (str): path of directory to store plots
        colmap (str): name of the python colour palette used, default = tab20.
        padcoords (list(float)): starting point for plot pad in x and y
            defines bottom and left margin sizes.
        padsize (list(float)): length of the plot pad as a fraction of the
            figure size in x and y directions (i.e. 1- margin sizes).

    '''
    # set colours, main figure and axes
    cmap = matplotlib.colormaps.get_cmap(colmap)
    colours = cmap.colors  # type: list
    fig = plt.figure(figsize=(11, 9))
    ax = fig.add_axes([padcoords[0], padcoords[1], padsize[0], padsize[1]])
    ax.set_prop_cycle(color=colours)

    lines = ["-", "--", "-.-"]
    channels = dataset.get_channels()
    bintime = str(dataset.metadata["time interval"])
    # convert responses to firing rates and plot them as lines
    for x in comparevar:
        yvals = {}
        for i, chan in enumerate(channels):
            yvals[chan] = [
                m*(1000./float(dataset.metadata["time interval"]))
                for m in means[constvar][x].values[i]]
            plt.plot(dataset.times, yvals[chan], label=x + " " + chan,
                     linestyle=lines[i])
    # set the legend and labels
    plt.legend()
    plt.xlabel("time [ms]")
    plt.ylabel("Mean Firing Rate [/s]")
    plt.title("Average Firing rate over beeID/Sensillum for "
              + constvar + ", bins = " + bintime + " ms")
    for ext in [".pdf", ".png"]:
        plt.savefig(outplotdir + constvar + "_ave_" + bintime + ext)
