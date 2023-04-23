import numpy as np

num_layers = 4
num_cells = 2

def print_point(file, point):
  file.write(f"Rh   {point[0]:.7f}   {point[1]:.7f}   {point[2]:.7f}\n")

def get_relaxed_coor(relaxed_coor_file_name)->list:
  begin_index = 0
  end_index = 0
  lines = []
  with open(f'./{relaxed_coor_file_name}.pwo', 'r') as fp:
    lines = fp.readlines()
    for i, line in enumerate(lines):
      if line.strip() == 'Begin final coordinates':
        begin_index = i
      if line.strip() == 'End final coordinates':
        end_index = i
    
  return lines[begin_index + 3: end_index]

def write_surf_coor(file_name: str, lines: list):

  with open(file_name, 'w') as file:
    for i in range(len(lines)):
      line = lines[i]
      if i < (num_cells**2 - 1) * num_layers:
        file.write(line)
      elif i >= (num_cells**2 - 1) * num_layers:
        line = line.replace('\n', '')
        file.write(line + '  0  0  0\n')

relaxed_coor_file_name = 'slab_2x2' # file.pwo with relaxed coordinates
relaxed_coor_list = get_relaxed_coor(relaxed_coor_file_name)
write_surf_coor('slab_relaxed_coor.dat', relaxed_coor_list)