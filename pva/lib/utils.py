from netaddr import *
from settings import IPS_BLACKLIST

def address_in_blacklist(ip):
    with open(IPS_BLACKLIST) as f:
        _networks = f.read().splitlines()
        return IPAddress(ip) in IPSet(_networks)
    return False
