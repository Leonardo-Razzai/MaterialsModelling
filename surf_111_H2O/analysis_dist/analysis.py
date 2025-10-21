import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

Ry_to_ev = 13.6057039763

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

class change_dist:
  def __init__(self) -> None:
    self.data = pd.read_csv(f'data/data_dist.dat', sep=' ')
    self.e_tot = self.data['E_tot'].to_numpy() * Ry_to_ev # in eV
    self.dist = self.data['dist'].to_numpy()
    self.far_energy = self.e_tot[-1]
    self.delta_E = self.e_tot - self.far_energy
    
  def plot_data(self):
    
    f_inter = interp1d(self.dist, self.delta_E, kind='cubic')
    d = np.linspace(self.dist[0], self.dist[-1], 100)
    
    _, ax = plt.subplots(1, 1, figsize=(9, 6))
    ax.plot(self.dist, self.e_tot - self.far_energy, 'o', color='red', markersize=7)
    ax.plot(d, f_inter(d), '-', color='red', lw=2.5)
    ax.set_title(r'$\Delta E$ approaching the surface', fontdict=title_font)
    ax.set_xlabel(r'dist ($\AA$)', fontdict=base_font)
    ax.set_ylabel(r'$\Delta E$ (eV)', fontdict=base_font)
    ax.grid()
    plt.savefig(f'../../../report/Figures/H2O/change_distance_H2O.png')
    plt.show()


result = change_dist()
result.plot_data()