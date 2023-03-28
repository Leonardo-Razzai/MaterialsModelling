import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

exp_result = pd.read_csv('en_vs_alat_exp.dat', sep=' ')
energy_exp = np.array(exp_result['energy(Ry)'])
alat_exp = np.array(exp_result['alat(a.u.)'])

fit_result = pd.read_csv('en_vs_alat_fit.dat', sep=' ')
energy_fit = np.array(fit_result['energy(Ry)'])
alat_fit = np.array(fit_result['alat(a.u.)'])

alat_min_en = alat_fit[energy_fit == np.min(energy_fit)][0]
print(f'lattice parameter corresponding to minimum energy: {alat_min_en} a.u.')

plt.plot(alat_fit, energy_fit, label='fit')
plt.plot(alat_exp, energy_exp, 'o', label='experimental data', color='red')
plt.xlabel('alat (a.u.)')
plt.ylabel('energy (Ry)')
plt.title('Energy vs lattice parameter')
plt.grid()
plt.legend()
plt.show()
