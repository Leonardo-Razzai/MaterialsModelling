import numpy as np
import pandas as pd

Ry_to_ev = 13.6057039763

class CO2_at_:
  def __init__(self, sym_ponit: str) -> None:
    self.sym_point = sym_ponit
    self.data = pd.read_csv(f'data/data_{sym_ponit}.dat', sep=' ')
    self.e_tot = float(self.data['E_tot'][0])
    self.e_slab = float(self.data['E_slab'][0])
    self.e_CO2 = float(self.data['E_CO2'][0])
    self.z_C = float(self.data['z_C'][0])
    self.z_last_layer = float(self.data['z_last_layer'][0])

    self.e_ad = (self.e_tot - self.e_slab - self.e_CO2) * Ry_to_ev 
    self.z_diff = self.z_C - self.z_last_layer
    
  def get_adsorption_energy(self):
    print(f'Adsorption energy for {self.sym_point} = {self.e_ad:.3f} ev')
  
  def get_CO2_distance(self):
    print(f'Distace from surface for {self.sym_point} = {self.z_diff:.3f} A')
  
  def get_all(self):
    print(f'\nCO2 at {self.sym_point}')
    print(f'e_tot = {self.e_tot}')
    print(f'z_C = {self.z_C}')
    print(f'z_last_layer = {self.z_last_layer}')
    
OT = CO2_at_('OT')
print(f'e_slab = {OT.e_slab}')
print(f'e_CO2 = {OT.e_CO2}')
OT.get_all()
OT.get_adsorption_energy()
OT.get_CO2_distance()

fcc = CO2_at_('fcc')
fcc.get_all()
fcc.get_adsorption_energy()
fcc.get_CO2_distance()

hcp = CO2_at_('hcp')
hcp.get_all()
hcp.get_adsorption_energy()
hcp.get_CO2_distance()