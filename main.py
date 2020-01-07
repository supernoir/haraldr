from bluetooth import discover_devices

print("performing inquiry...")

nearby_devices = discover_devices(lookup_names = True)

print("found %d devices" % len(nearby_devices))

for name, addr in nearby_devices:
     print(" %s - %s" % (addr, name))
