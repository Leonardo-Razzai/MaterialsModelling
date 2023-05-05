#!/bin/bash

# Create  a file called data_$1.dat with total final energy (E_tot)
# energy of 2x2 slab (E_slab), energy of isolated H2O (E_H2O) and 
# coordinates z_O and mean z af the last layer

sym_point=$1
echo "E_tot E_slab E_H2O z_O z_last_layer" > data_$sym_point.dat
E_tot=$(grep -a Final ../H2O_at_$sym_point.pwo | awk '{print $4}')
E_slab=$(grep -a Final ../slab_2x2.pwo | awk '{print $4}')
E_H2O=$(grep -a Final ../../H2O/H2O.pwo | awk '{print $4}')
coor=$(python3 get_coordinates.py $sym_point)

echo "$E_tot $E_slab $E_H2O $coor" >> data_$sym_point.dat
