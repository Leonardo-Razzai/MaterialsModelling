#!/bin/bash

# Create  a file called data_$1.dat with total final energy (E_tot)
# energy of 2x2 slab (E_slab), energy of isolated CO2 (E_CO2) and 
# coordinates z_C and mean z af the last layer

sym_point=$1
echo "E_tot E_slab E_CO2 z_C z_last_layer" > data_$sym_point.dat
E_tot=$(grep -a Final ../CO2_at_$sym_point.pwo | awk '{print $4}')
E_slab=$(grep -a Final ../slab_2x2.pwo | awk '{print $4}')
E_CO2=$(grep -a Final ../../CO2/CO2_relax.pwo | awk '{print $4}')
coor=$(python3 get_coordinates.py $sym_point)

echo "$E_tot $E_slab $E_CO2 $coor" >> data_$sym_point.dat
