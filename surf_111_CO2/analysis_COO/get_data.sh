#!/bin/bash
sym_point="hcp"
echo sym_point $sym_point

FILE_TO_WRITE="data/data_$sym_point.dat"
echo "E_tot z_C z_last_layer" > $FILE_TO_WRITE
E_tot=$(grep ! ../COO_at_$sym_point.pwo | tail -1 | awk '{print $5}')
coor=$(python3 get_coordinates.py $sym_point)
echo "$E_tot $coor" >> $FILE_TO_WRITE
