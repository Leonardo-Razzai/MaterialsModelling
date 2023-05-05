#!/bin/bash

sym_point=$1
FILE_TO_WRITE=data/data_$sym_point.dat
echo "E_tot z_O z_last_layer" > $FILE_TO_WRITE
E_tot=$(grep -a Final ../OHH_at_$sym_point.pwo | tail -1 | awk '{print $4}')
coor=$(python3 get_coordinates.py $sym_point)

echo "$E_tot $coor" >> $FILE_TO_WRITE
