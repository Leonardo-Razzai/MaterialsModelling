import numpy as np
import pandas as pd

Ry_to_ev = 13.6057039763
e_i = -2773.3900844787 # Ry

class OHH_at_:
  def __init__(self, sym_ponit: str) -> None:
    self.sym_point = sym_ponit
    self.data = pd.read_csv(f'data/data_{sym_ponit}.dat', sep=' ')
    self.e_tot = float(self.data['E_tot'][0])
    self.z_O = float(self.data['z_O'][0])
    self.z_last_layer = float(self.data['z_last_layer'][0])

    self.e_diss = (self.e_tot - e_i) * Ry_to_ev 
    self.z_diff = self.z_O - self.z_last_layer
    
  def get_dissociation_energy(self):
    print(f'Dissociation energy for {self.sym_point} = {self.e_diss:.5f} ev')
  
  def get_OHH_distance(self):
    print(f'Distace from surface for {self.sym_point} = {self.z_diff:.3f} A')

OT = OHH_at_('OT')
OT.get_dissociation_energy()
OT.get_OHH_distance()

fcc = OHH_at_('fcc')
fcc.get_dissociation_energy()
fcc.get_OHH_distance()

hcp = OHH_at_('hcp')
hcp.get_dissociation_energy()
hcp.get_OHH_distance()