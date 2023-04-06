from pprint import pprint

#Example with list
result = [
    ["FastEthernet0/0", "15.0.15.1"],
    ["FastEthernet0/0", "15.0.15.1"],
    ["FastEthernet0/0", "15.0.15.1"],
]

result_list = []

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_list = line.split()
        
        #if line_list: # same as - if len(line_list !=0)
        #    str_index_0 = line_list[0]
        #    if str_index_0[-1].isdigit():
        #        intf_ip_list = (line_list[0:2])
        #        result_list.append(intf_ip_list)
        
        #The above example is the same but longer
        if line_list and line_list[0][-1].isdigit():
            intf_ip_list = (line_list[0:2])
            result_list.append(intf_ip_list)

pprint(result_list)

##################################################################

#Example with dictionary
result = {
    "FastEthernet0/0": "15.0.15.1",
    "FastEthernet0/0": "15.0.15.1",
    "FastEthernet0/0": "15.0.15.1",
}

result_dict = {}

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0][-1].isdigit():
            intf, ip = line_list[:2]
            result_dict[intf] = ip

pprint(result_dict)





