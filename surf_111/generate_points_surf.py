import numpy as np
import sys

def print_point(file, point):
  file.write(f"Rh   {point[0]:.7f}   {point[1]:.7f}   {point[2]:.7f}\n")
  
def get_celldm3(points):
  empty_space = 12 # Angstrom
  last_point = points[len(points)-1]
  zmax = last_point[2]
  celldm3 = (zmax + empty_space) / a
  return celldm3
 
n_layers = int(sys.argv[1])

a_bohr = 7.2447 / np.sqrt(2)
a = a_bohr * 0.529177249 # Lattice parameter Angstrom
a2 = a * np.array([1/2, np.sqrt(3)/2, 0])
a3 = a * np.array([0, 0, np.sqrt(6)])

base_points = [
  a * np.array([0, 0, 0]), # A
  a * np.array([1/2, -np.sqrt(3) / 6, 0]), # B
  a * np.array([1/2, np.sqrt(3) / 6, 0]), # C
]

points = []
with open('points.txt', 'w') as file:
  for i in range(n_layers):
    point_index = i % 3
    selected_point = base_points[point_index]
    inc_point = selected_point + i * a3 / 3
    points.append(inc_point)
    print_point(file=file, point=inc_point)

<<<<<<<< HEAD:surf_111/generate_points.py
print(f"celldm(1) = {a_bohr:.6f}")
print("Bulk: ")
print(f"celldm(3) = {np.sqrt(6):.6f}")
print("Surface: ")
print(f"celldm(3) = {get_celldm3(points):.6f}")
========
# print(f"celldm(1) = {a_bohr:.6f}")
# print(f"celldm(3) = {get_celldm3(points):.6f}")
>>>>>>>> 05e8e796b4e4c5da48ff6daacd7ccc819d4aea83:surf_111/generate_points_surf.py
