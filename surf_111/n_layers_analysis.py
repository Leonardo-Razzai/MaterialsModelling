import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

ev_per_Ry = 13.6057039763

en_vs_nlayers_df = pd.read_csv('en_vs_nlayers.dat', sep=' ')
n_layers = np.array(en_vs_nlayers_df['n_layers'])
energy = np.array(en_vs_nlayers_df['energy(Ry)']) * ev_per_Ry

ebulk_Ry = -513.5794157304 / 3
ebulk = ebulk_Ry * ev_per_Ry # enenrgy per atom in bulk (ev)
print(f"Energy per atom = {ebulk_Ry:.4f} Ry")

a_bohr = 7.2447 / np.sqrt(2)
a = a_bohr * 0.529177249 # lattice param in A
A = np.sqrt(3) / 2 * a**2 # area in A**2
print(f'Area = {A:.3f} A^2')

surf_energy = 0.5 / A * (energy - n_layers * ebulk) * 16.0217663 # surface energy in J/m**2
print('surface energy:\n', surf_energy)

delta_surf_en = surf_energy[:-1] - surf_energy[1:]
n_layers_delta = n_layers[:-1]

f_inter = interp1d(n_layers_delta, delta_surf_en, kind='cubic')
n_layers_plot = np.linspace(np.min(n_layers_delta), np.max(n_layers_delta), 200)

f_inter_surfE = interp1d(n_layers[:-1], surf_energy[:-1], kind='cubic')
n_layers_surf_plot =  np.linspace(3, 8, 200)

MEDIUM_SIZE = 22
BIGGER_SIZE = 25

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

_, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.plot(n_layers_delta, delta_surf_en, 'o', color='royalblue')
ax.plot(n_layers_plot, f_inter(n_layers_plot), '--', color='royalblue')
ax.set_title(r'Surface energy with increasing number of layers', fontdict=title_font)
ax.set_xlabel('n_layers', fontdict=base_font)
ax.set_ylabel(r'$\Delta E$ (J/$m^2$)', fontdict=base_font)
ax.grid()
plt.savefig(f'../../report/Figures/surf_delta_energy.png')
plt.show()

_, ax = plt.subplots(1, 1, figsize=(11, 8))
ax.plot(n_layers[:-1], surf_energy[:-1], 'o', color='royalblue')
ax.plot(n_layers_surf_plot, f_inter_surfE(n_layers_surf_plot), '--', color='royalblue')
ax.set_title(r'Surface energy with increasing number of layers', fontdict=title_font)
ax.set_xlabel('n_layers', fontdict=base_font)
ax.set_ylabel(r'E (J/$m^2$)', fontdict=base_font)
ax.grid()
plt.savefig(f'../../report/Figures/surf_energy.png')
plt.show()
