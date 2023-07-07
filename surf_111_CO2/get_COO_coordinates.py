import numpy as np
import sys

num_layers = 4
num_cells = 2
num_atoms_per_layer = num_cells * num_cells

a_bohr = 7.2447 / np.sqrt(2)
a = a_bohr * 0.529177249
a1 = a * np.array([1, 0, 0])
a2 = a * np.array([-1/2, np.sqrt(3)/2, 0])

sym_point = sys.argv[1]

def print_atom_coor(file, 
                    atom: str, 
                    coor: np.ndarray, 
                    write=True):
  
  if write == True:
    file.write(f"{atom}   {coor[0]:.7f}   {coor[1]:.7f}   {coor[2]:.7f}\n")
  else:
    return f"{atom}   {coor[0]:.7f}   {coor[1]:.7f}   {coor[2]:.7f}"
  
def get_relaxed_coor(relaxed_coor_file_name)->list:
  '''
  Given final coordinates in relaxed_coor_file_name.pwo
  a list of ndarrays, each containing a coordinate, is returned.
  '''
  begin_index = 0
  end_index = 0
  relaxed_coor_list = []
  with open(f'./{relaxed_coor_file_name}.pwo', 'r') as fp:
    lines = fp.readlines()
    for i, line in enumerate(lines):
      if line.strip() == 'Begin final coordinates':
        begin_index = i
      if line.strip() == 'End final coordinates':
        end_index = i
    
    for i in range(begin_index + 3, end_index):
      line = lines[i]
      coor_string = line.split()[1:]
      relaxed_coor = np.array([
        float(coor_string[0]),
        float(coor_string[1]),
        float(coor_string[2])
      ])
      
      relaxed_coor_list.append(relaxed_coor)
    
  return relaxed_coor_list

def write_surf_coor(file, 
                    surf_coor_list: list):
  
  for i in range(len(surf_coor_list)):
    coor = surf_coor_list[i]
    if i < (num_cells**2 - 1) * num_layers:
      print_atom_coor(file, 'Rh', coor)
    elif i >= (num_cells**2 - 1) * num_layers:
      line = print_atom_coor(file, 'Rh', coor, write=False)
      file.write(line + '  0  0  0\n')

def get_last_layers(surf_coor_list: list,
                    num=3) -> list:
  '''
  Returns a list containing the last num layers of the surface
  '''
  layers =  []
  for i in range(num):
    layers.append(surf_coor_list[i * num_atoms_per_layer: (i + 1) * num_atoms_per_layer])
  
  return layers
  
def write_OHH_coor(file, 
                   surf_coor_list: list,
                   sym_point='OT'):
  
  bond_length = 1.1770702732 # A
  
  last_layers = get_last_layers(surf_coor_list, num=3)
  A = last_layers[0][3]
  C = last_layers[1][3]
  B = last_layers[2][3]
  
  height_from_surf = 2.442 # A
  CO2_height = A[2] + height_from_surf

  # OH
  OT_offset = np.array([A[0], A[1], CO2_height])
  C_base = np.array([0, 0, 0])
  O1_base = np.array([1, 0, 0]) * bond_length
  O2_base = np.array([-1, 0, 0]) * bond_length
  
  C_coor = C_base + OT_offset
  O1_coor = O1_base + OT_offset
  
  # H
  if sym_point == 'OT':
    O2_coor = np.array([A[0], A[1], CO2_height]) + a2
  elif sym_point == 'fcc':
    O2_coor = np.array([B[0], B[1], CO2_height])
  elif sym_point == 'hcp':
    O2_coor = np.array([C[0], C[1], CO2_height]) - a1
  else:
    print('Choose a correct symmetry point:\n- OT\n- fcc\n- hcp')
  
  print_atom_coor(file, atom='O', coor=O1_coor + a1 + a2)
  print_atom_coor(file, atom='O', coor=O2_coor + a1 + a2)
  print_atom_coor(file, atom='C', coor=C_coor + a1 + a2)


relaxed_coor_file_name = 'slab_2x2' # file.pwo with relaxed coordinates
relaxed_coor_list = get_relaxed_coor(relaxed_coor_file_name)

with open(f'COO_at_{sym_point}-coor.dat', 'w') as file:
  write_OHH_coor(file, relaxed_coor_list, sym_point=sym_point)
  write_surf_coor(file, relaxed_coor_list)