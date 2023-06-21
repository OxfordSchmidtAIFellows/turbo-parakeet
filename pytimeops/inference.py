
import numpy as np
import pytimeops as pto

import statsmodels.api as sm

import matplotlib.pyplot as plt







def main():
    y = pto.read_file('Data/20ms_bins_dataframe.csv', 20)
    print(y)

    y.filter('concentration', ['100mM'])

    for i in range(100):
        for j in range(2):
            x = y.dataset[i]
            z = x.values[j]

            print(z)

            model = sm.tsa.SARIMAX(z, order=(3, 0, 0), trend='ct', measurement_error=False)
            result = model.fit()

            print(result.summary())

            intercept, drift = result.mlefit.params[0:2]
            ar1 = result.arparams[0]

            mean = result.get_prediction()._results._predicted_mean
            var = result.get_prediction()._results._var_pred_mean

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            tplot = np.linspace(0, 20*len(z), 50)
            ax.plot(tplot, z, 'x-', label='Data', color='k', zorder=100)

            ax.plot(tplot[1:], mean[1:], label='Mean (fit)', color='seagreen')
            ax.fill_between(tplot[1:], (mean-2*np.sqrt(var))[1:], (mean+2*np.sqrt(var))[1:], alpha=0.25, color='seagreen')
            ax.legend()

            ax.set_xlabel('Time (ms)')
            ax.set_ylabel('Response')

            fig.suptitle('Drift={:4f}, AR1_coeff={:4f}'.format(drift, ar1).replace('-', '−'))
            plt.show()

    return



if __name__ == '__main__':
    main()
