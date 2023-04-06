# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip = input("Enter IP: ")
octets = ip.split(".")

increment = 0

if len(octets) == 4 and ip.count(".") == 3:
    for each_octet in octets:
        if each_octet.isnumeric():
            if int(each_octet) in range(256):
                increment += 1

if increment == 4:
    if int(octets[0]) in range(224):
        print("unicast")
    elif int(octets[0]) in range(224, 240):
        print("mulicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else:
    print("Invalid IP address")
