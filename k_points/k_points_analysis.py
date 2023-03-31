import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

df = pd.read_csv('en_vs_kpoints_1.dat', sep=' ')
energy = np.array(df['energy(Ry)'])
k_points = np.array(df['k_points'])
Delta_E = (energy - energy[-1]) * 13.6 *1000 # in mev

f_inter = interp1d(k_points, Delta_E, kind='cubic')

base_font = {'family': 'serif',
        'color':  'black',
        'size': 12,
        }

title_font = {'family': 'serif',
        'color':  'black',
        'size': 19,
        'weight' : 'normal'
        }

k = np.linspace(np.min(k_points), np.max(k_points), 300)
_, ax = plt.subplots(1, 1, figsize=(9, 6))
ax.plot(k_points, Delta_E, 'o', color='royalblue')
ax.plot(k, f_inter(k), '-', color='royalblue')
ax.set_title(r'$\Delta E$ (mev) vs number of k-points', fontdict=title_font)
ax.set_xlabel('k-points', fontdict=base_font)
ax.set_ylabel(r'$\Delta E$ (mev)', fontdict=base_font)
ax.grid()
plt.show()