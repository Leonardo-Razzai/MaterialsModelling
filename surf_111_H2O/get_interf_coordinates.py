import numpy as np
import sys

num_layers = 4
num_cells = 2
num_atoms_per_layer = num_cells * num_cells
# NB: give integer numbers as .0
height_from_surf = float(sys.argv[1])

a_bohr = 7.2447 / np.sqrt(2)
a = a_bohr * 0.529177249
a1 = a * np.array([1, 0, 0])
a2 = a * np.array([-1/2, np.sqrt(3)/2, 0])

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
      file.write(line + '  1  1  0\n')

def get_last_layers(surf_coor_list: list,
                    num=3) -> list:
  '''
  Returns a list containing the last num layers of the surface
  '''
  layers =  []
  for i in range(num):
    layers.append(surf_coor_list[i * num_atoms_per_layer: (i + 1) * num_atoms_per_layer])
  
  return layers
  
def write_H2O_coor(file, 
                   surf_coor_list: list):
  
  bond_length = 0.9815 # A
  bond_angle = 103.432 / 180 * np.pi # rad
  
  last_layers = get_last_layers(surf_coor_list, num=3)
  OT = last_layers[0][3]

  H2O_height = OT[2] + height_from_surf
  
  O_base = np.array([0, 0, 0])
  H1_base = np.array([1, 0, 0]) * bond_length
  H2_base = np.array([np.cos(bond_angle), np.sin(bond_angle), 0]) * bond_length
  
  offset = np.array([OT[0], OT[1], H2O_height]) + a1 + a2
  
  O_coor = O_base + offset
  H1_coor = H1_base + offset
  H2_coor = H2_base + offset
  
  print_atom_coor(file, atom='H', coor=H1_coor)
  print_atom_coor(file, atom='H', coor=H2_coor)
  line = print_atom_coor(file, atom='O', coor=O_coor, write=False)
  file.write(line + '  1  1  0\n')

relaxed_coor_file_name = 'slab_2x2' # file.pwo with relaxed coordinates
relaxed_coor_list = get_relaxed_coor(relaxed_coor_file_name)

with open(f'interf_at_{height_from_surf}-coor.dat', 'w') as file:
  coor_last_Rh = relaxed_coor_list[0:3]
  slab_thickness = np.mean(coor_last_Rh, axis=0)[2]
  super_slab_coor = -np.array(relaxed_coor_list) + np.array([0, 0, 2*height_from_surf + 2*slab_thickness])
  super_slab_coor = np.flip(super_slab_coor, axis=0)
  write_surf_coor(file, super_slab_coor)
  write_H2O_coor(file, relaxed_coor_list)
  write_surf_coor(file, relaxed_coor_list)