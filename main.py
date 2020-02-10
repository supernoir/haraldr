from bluetooth import discover_devices
from datetime import datetime

def getCurrentTime():
     return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def printTimeStamp():
     print("===== %s =====" % getCurrentTime())

def discover():
     printTimeStamp()

     nearby_devices = discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

     try:
          if nearby_devices:
               print("Found %d device(s)" % len(nearby_devices))
               for addr, name in nearby_devices:
                    print("Name: %s \t Address: %s" % (name, addr))
          else:
               print("No devices found.")
     except UnicodeEncodeError:
          print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))



discover()