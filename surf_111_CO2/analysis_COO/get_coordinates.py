import numpy as np
import sys

sym_point = sys.argv[1]
file_name = f'../COO_at_{sym_point}.pwo'

def get_relaxed_coor(relaxed_coor_file_name)->list:
  begin_index = 0
  end_index = 0
  relaxed_coor_list = []
  with open(relaxed_coor_file_name, 'r') as fp:
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

def print_coor(file, coor):
  file.write(f'{coor[0]} {coor[1]} {coor[2]}\n')
  
def write_coor_to_file(coordinates, file_name=f'data/{sym_point}_coor.dat'):

  with open(file_name, 'w') as file:
    for coor in coordinates:
      print_coor(file, coor)

def write_coor(coordinates):
  coor_C = coordinates[2]
  coor_last_Rh = coordinates[3:7]
  mean_z = np.mean(coor_last_Rh, axis=0)[2]
  print(f'{coor_C[2]} {mean_z}')
  
coordinates = get_relaxed_coor(file_name)
write_coor_to_file(coordinates)
write_coor(coordinates)