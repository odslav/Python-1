interface = {"description": "ISP", "ip":"10.1.1.1", "mask":"255.255.255.0", "gateway":"10.1.1.255"}
print(interface["ip"])

interface["description"] = "Spectrum"
print(interface["description"])

interface["mtu"] = 1500

print(interface)
