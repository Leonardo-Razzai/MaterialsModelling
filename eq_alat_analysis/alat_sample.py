import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
bohr_to_A = 0.529177249

class ecut_sample:
  def __init__(self, ecut: int) -> None:
    '''
    This class is aimed to analyze data resulting from Quantum Espresso simulation
    in order to find the equilibrium lattice parameter of a solid by fitting with
    Murnagham state functioin
    
    Attributes
    ----------
    ecut : int
           Cut off energy selected in the .pwi file.
    energy_exp : ndarray
                 Total energies (Ry) resulting from simulations (total enenrgy in .pwo file)
    alat_exp : ndarray
               Lattice parameters (a.u.) used for the simulations (celldm(1) in .pwi files)
    energy_fit : ndarray
                 Total energies (Ry) resulting from fit (found in murn_<E>.out files)
    alat_fit : ndarray
               Lattice parameters (a.u.) resulting from fit (found in murn_<E>.out files)         
    
    '''
    self.ecut = ecut
    
    exp_result = pd.read_csv(f'ecut_{ecut}/en_vs_alat_exp_{ecut}.dat', sep=' ')
    self.energy_exp = np.array(exp_result['energy(Ry)'])
    self.alat_exp = np.array(exp_result['alat(a.u.)'])

    fit_result = pd.read_csv(f'ecut_{ecut}/en_vs_alat_fit_{ecut}.dat', sep=' ')
    self.energy_fit = np.array(fit_result['energy(Ry)'])
    self.alat_fit = np.array(fit_result['alat(a.u.)'])

    self.min_energy = np.min(self.energy_fit)
    self.alat_min_en = self.alat_fit[self.energy_fit == self.min_energy][0]
    
  def plot_fit(self, ax, color='blue'):
    offset = 171
    ax.plot(self.alat_fit * bohr_to_A, self.energy_fit + offset, label=f'ecut= {self.ecut} Ry', color=color, linewidth=2)
    ax.plot(self.alat_exp * bohr_to_A, self.energy_exp + offset, 'o', color=color, markersize=8)