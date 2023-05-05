import numpy as np
import pandas as pd

Ry_to_ev = 13.6057039763

class H2O_at_:
  def __init__(self, sym_ponit: str) -> None:
    self.sym_point = sym_ponit
    self.data = pd.read_csv(f'data/data_{sym_ponit}.dat', sep=' ')
    self.e_tot = float(self.data['E_tot'][0])
    self.e_slab = float(self.data['E_slab'][0])
    self.e_H2O = float(self.data['E_H2O'][0])
    self.z_O = float(self.data['z_O'][0])
    self.z_last_layer = float(self.data['z_last_layer'][0])

    self.e_ad = (self.e_tot - self.e_slab - self.e_H2O) * Ry_to_ev 
    self.z_diff = self.z_O - self.z_last_layer
    
  def get_adsorption_energy(self):
    print(f'Adsorption energy for {self.sym_point} = {self.e_ad:.3f} ev')
  
  def get_H2O_distance(self):
    print(f'Distace from surface for {self.sym_point} = {self.z_diff:.3f} A')
  
  def get_all(self):
    print(f'\nH2O at {self.sym_point}')
    print(f'e_tot = {self.e_tot}')
    print(f'z_O = {self.z_O}')
    print(f'z_last_layer = {self.z_last_layer}')
    
OT = H2O_at_('OT')
print(f'e_slab = {OT.e_slab}')
print(f'e_H2O = {OT.e_H2O}')
OT.get_all()
OT.get_adsorption_energy()
OT.get_H2O_distance()

fcc = H2O_at_('fcc')
fcc.get_all()
fcc.get_adsorption_energy()
fcc.get_H2O_distance()

hcp = H2O_at_('hcp')
hcp.get_all()
hcp.get_adsorption_energy()
hcp.get_H2O_distance()