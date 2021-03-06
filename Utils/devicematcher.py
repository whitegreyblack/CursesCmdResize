#!/usr/bin/env python
'''
Author  : Sam Whang
Filename: DeviceMatcher.py
License : MIT
Usage   : compares interface signatures and serializes them to
          an abbreviated signature
'''
import re

# any devices matching the first indices in each list
# will conform to the second index after pattern match
interfaces = [
    [["TenGigabitEthernet", "Te"], "Te"],
    [["GigabitEthernet", "Gi"], "Gi"],
    [["FastEthernet", "Fa"], "Fa"],
    [["Ethernet", "Eth"], "Eth"],
    [["Port-channel", "Po"], "Po"],
    [["Serial"], "Ser"],
]

def converter(devicename):
    '''
    Compares string input with regex pattern and checks result.
    If result is true, go through list of interfaces to find exact match
    On false result, print error
    '''
    pattern = r'([a-zA-Z\-]*)(\d+[\/\d\:]*)'
    result = re.match(pattern, devicename)
    if result:
        device, number = list(result.groups())
        stop = False
        
        # iterate through interfaces to find matches -- stops when found
        for interface, conversion in interfaces:
            for i in interface:
                # sanitize the strings before comparison
                if device.lower() == i.lower():
                    print(f'Converting: {devicename} -> {conversion}{number}')
                    stop = True
            if stop:
                break
    else:
        print(f'No known conversion names for this device: {devicename}')

# Simple test cases

# tests should pass
converter('GigabitEthernet1/3')
converter('tengigabitethernet7/1/25')
converter('Serial1/0/0/15:1')

# failure -- no match
converter('asdfaf')
