# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
from re import A, sub


subnet = input("Enter IP subnet: ")
octet = subnet.split(".")
octet1 = int(octet[0])
octet2 = int(octet[1])
octet3 = int(octet[2])
octet4_split = octet[3].split("/")
octet4 = int(octet4_split[0])

octets_prefix = (octet[0:3]) + octet[3].split("/")
prefix = octets_prefix[-1]
mask_bin = int(prefix) * "1" + (32 - int(prefix)) * "0"
mask_bin_split = mask_bin
mask_oct1 = int(mask_bin_split[0:8], 2)
mask_oct2 = int(mask_bin_split[8:16], 2)
mask_oct3 = int(mask_bin_split[16:24], 2)
mask_oct4 = int(mask_bin_split[24:32], 2)

print(f"Network:\n{octet1:<10}{octet2:<10}{octet3:<10}{octet4:<10}\n{octet1:08b}  {octet2:08b}  {octet3:08b}  {octet4:08b}\n")
print(f"Mask:\n/{prefix}\n{mask_oct1:<8}  {mask_oct2:<8}  {mask_oct3:<8}  {mask_oct4:<8}\n{mask_oct1:08b}  {mask_oct2:08b}  {mask_oct3:08b}  {mask_oct4:08b}")

