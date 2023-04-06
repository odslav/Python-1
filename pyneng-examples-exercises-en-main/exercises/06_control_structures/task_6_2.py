# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip = input("Enter IP: ")
octets = ip.split(".")

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





