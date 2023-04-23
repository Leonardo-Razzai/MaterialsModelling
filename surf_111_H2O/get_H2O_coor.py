import numpy as np

O_coor = 
def print_atom_coor(file, atom: str, coor: np.ndarry):
  file.write(f"{atom}   {coor[0]:.7f}   {coor[1]:.7f}   {coor[2]:.7f}\n")

