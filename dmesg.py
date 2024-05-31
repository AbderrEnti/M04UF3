#!/usr/bin/python3

import subprocess
 
dmesg = subprocess.getoutput("dmesg")

dmesg_data = []
for dmesg_line in dmesg.splitlines():
    dmesg_temp = dmeg_line.split("[")[1]
    dmesg_time = dmesg_temp.split("]")[0]
    dmesg_temp = dmesg_temp.split("]")[1]
    dmesg_temp = dmesg_temp.split(":")
    dmesg_module = dmesg_temp[0]
    dmesg_info = ""

    if len(dmesg_temp) >1:
        dmesg_info = dmesg_temp[1]
   
   dmesg_data.append([dmesg_time, dmesg_module, dmesg_info])

print(dmesg_data)

