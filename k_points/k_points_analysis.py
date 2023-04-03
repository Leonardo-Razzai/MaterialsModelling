import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

offset = 0 # offset value for k-vectors

df = pd.read_csv(f'en_vs_kpoints_{offset}.dat', sep=' ')
energy = np.array(df['energy(Ry)'])
k_points = np.array(df['k_points'])
Delta_E = (energy[1:] - energy[:-1]) * 13.6 *1000 # in mev

f_inter = interp1d(k_points[:-1], Delta_E, kind='cubic')

MEDIUM_SIZE = 17
BIGGER_SIZE = 20

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

base_font = {'family': 'serif',
        'color':  'black',
        'size': MEDIUM_SIZE,
        }

title_font = {'family': 'serif',
        'color':  'black',
        'size': BIGGER_SIZE,
        'weight' : 'bold'
        }

k = np.linspace(np.min(k_points[:-1]), np.max(k_points[:-1]), 300)
_, ax = plt.subplots(1, 1, figsize=(9, 6))
ax.plot(k_points[:-1], Delta_E, 'o', color='royalblue')
ax.plot(k, f_inter(k), '-', color='royalblue')
ax.set_title(r'$\Delta E$ between subsequent number of k-points', fontdict=title_font)
ax.set_xlabel('k-points', fontdict=base_font)
ax.set_ylabel(r'$\Delta E$ (mev)', fontdict=base_font)
ax.grid()
plt.savefig(f'../../report/Figures/k_points_off{offset}.png')
plt.show()
