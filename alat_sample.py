import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ecut_sample:
  def __init__(self, ecut: int) -> None:
    
    self.ecut = ecut
    
    exp_result = pd.read_csv(f'ecut_{ecut}/en_vs_alat_exp_{ecut}.dat', sep=' ')
    self.energy_exp = np.array(exp_result['energy(Ry)'])
    self.alat_exp = np.array(exp_result['alat(a.u.)'])

    fit_result = pd.read_csv(f'ecut_{ecut}/en_vs_alat_fit_{ecut}.dat', sep=' ')
    self.energy_fit = np.array(fit_result['energy(Ry)'])
    self.alat_fit = np.array(fit_result['alat(a.u.)'])

    self.alat_min_en = self.alat_fit[self.energy_fit == np.min(self.energy_fit)][0]
    
  def plot_fit(self, color='blue'):
    plt.plot(self.alat_fit, self.energy_fit, label=f'Ecut = {self.ecut}', color=color)
    plt.plot(self.alat_exp, self.energy_exp, 'o', color=color)
   