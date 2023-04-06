# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip = input("Enter IP: ")

correct_ip = False

while correct_ip == False:
    octets = ip.split(".")
    increment = 0
    if len(octets) == 4:
        for each_octet in octets:
            if each_octet.startswith("0") and len(each_octet) > 1:
                break
            if each_octet.isnumeric() and int(each_octet) in range(256):
                increment += 1
                if increment >= 4:
                    correct_ip = True
    if not correct_ip:
        ip = input("Invalid IP address. Enter IP again: ")


if correct_ip:
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