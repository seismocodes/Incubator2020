"""
This module contains a function to plot catalogs
of low-frequency earthquakes
"""
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle

from datetime import datetime, timedelta
from math import floor

def plot_catalogs(family_file, window = 86400):
    """
    Plot catalogs for all the families in input file

    Input:
        type family_file = string
        family_file = File containing the list of LFE families
        type window = float
        window = Duration (s) of the time window where we compute the nmber of LFEs
    Output:
        None
    """
    if int(window) == 3600:
        name = 'hours'
    elif int(window) == 86400:
        name = 'days'
    else:
        name = 'unknown'

    families = pd.read_csv(family_file, \
        sep=r'\s{1,}', header=None, engine='python')
    families.columns = ['family', 'stations']

    # Loop on families
    for i in range(0, len(families)):

        # Read catalogs
        namedir = 'output/' + families['family'].iloc[i]
        days = os.listdir(namedir)
        catalogs = list()
        for day in days:
            df = pd.read_csv(namedir + '/' + day, index_col=0)
            catalogs.append(df)
        catalog = pd.concat(catalogs, ignore_index=True)

        # Create time series
        df = pd.DataFrame({'year':catalog['year'], \
            'month':catalog['month'], 'day':catalog['day']})
        date = pd.to_datetime(df)
        t1 = date.min()
        t2 = date.max()
        tbegin = datetime(t1.year, t1.month, t1.day, 0, 0, 0, 0)
        tend = datetime(t2.year, t2.month, t2.day, 0, 0, 0, 0)
        dt = tend - tbegin
        duration = dt.days * 86400.0 + dt.seconds + dt.microseconds * 0.000001
        nw = int(duration / window)
        X = np.zeros(nw, dtype=int)

        # Loop on LFEs
        for j in range(0, len(catalog)):
            myYear = catalog['year'].iloc[j]
            myMonth = catalog['month'].iloc[j]
            myDay = catalog['day'].iloc[j]
            myHour = catalog['hour'].iloc[j]
            myMinute = catalog['minute'].iloc[j]
            mySecond = int(floor(catalog['second'].iloc[j]))
            myMicrosecond = int(1000000.0 * (catalog['second'].iloc[j] - mySecond))
            t = datetime(myYear, myMonth, myDay, myHour, myMinute, mySecond, \
                myMicrosecond)
            # Add LFE to appropriate time window
            if ((tbegin <= t) and (t < tbegin + timedelta(seconds=nw * window))):
                dt = t - tbegin
                duration = dt.days * 86400.0 + dt.seconds + dt.microseconds * \
                    0.000001
                index = int(duration / window)
                X[index] = X[index] + 1

        # Plot figure
        plt.figure(1, figsize=(10, 6))
        params = {'xtick.labelsize':16,
                  'ytick.labelsize':16}
        pylab.rcParams.update(params) 
        plt.stem(np.arange(0, len(X)), X, 'k-', markerfmt=' ', basefmt=' ')
        plt.xlim([-0.5, len(X) - 0.5])
        plt.xlabel('Time ({}) since {:4d}/{:2d}/{:2d}'. \
            format(name, tbegin.year, tbegin.month, tbegin.day), fontsize=20)
        plt.ylabel('Number of LFEs', fontsize=20)
        plt.title('Family {} ({:d} LFEs)'.format(families['family'].iloc[i], np.sum(X)), \
            fontsize=24)
        plt.savefig('output/' + families['family'].iloc[i] + '.eps', format='eps')
        plt.close(1)

if __name__ == '__main__':
    
    family_file = '../examples/families_permanent.txt'
    window = 86400
    plot_catalogs(family_file, window)
