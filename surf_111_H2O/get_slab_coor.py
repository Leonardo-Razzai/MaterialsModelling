import numpy as np

def print_point(file, point):
  file.write(f"Rh   {point[0]:.7f}   {point[1]:.7f}   {point[2]:.7f}\n")

def get_relaxed_coor(relaxed_coor_file_name)->list:
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

def write_new_coor(file_name='new_coor.dat'):
  
  a_bohr = 7.2447 / np.sqrt(2)
  a = a_bohr * 0.529177249 # Lattice parameter Angstrom
  a1 = a * np.array([1, 0, 0])
  a2 = a * np.array([-1/2, np.sqrt(3)/2, 0])

  new_coord_list = []
  for relaxed_coor in relaxed_coor_list:
    new_coord_list.append(relaxed_coor)
    new_coord_list.append(relaxed_coor + a1)
    new_coord_list.append(relaxed_coor + a2)
    new_coord_list.append(relaxed_coor + a1 + a2)

  with open(file_name, 'w') as file:
    size = len(new_coord_list)
    for i in range(size):
      coor = new_coord_list[size-1 - i]
      print_point(file, coor)

relaxed_coor_file_name = 'n_layers4' # file.pwo with relaxed coordinates
relaxed_coor_list = get_relaxed_coor(relaxed_coor_file_name)
write_new_coor('surf_coor.dat')