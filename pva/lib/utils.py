try:
   import cPickle as pickle
except:
   import pickle
import os
from netaddr import *
from settings import IPS_BLACKLIST


def address_in_blacklist(ip):
    """
    Check if IP address is in black list
    :param ip: IPv4 address
    :return Boolean:
    """
    with open(IPS_BLACKLIST) as f:
        _networks = f.read().splitlines()
        return IPAddress(ip) in IPSet(_networks)
    return False


def dump_object(filename, object):
    """
    Serialize and save object
    :param filename: full path to file
    :param object: object to be dumped
    """
    with open(filename, 'wb') as f:
        pickle.dump(object, f)


def load_dumped_object(filename):
    """
    Load, deserialize and returns object from file
    :param filename: full path to file
    :return Object:
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)


def create_directory(dirname):
    """
    Create directory
    :param dirname: full path to directory
    """
    if not os.path.exists(dirname):
        os.makedirs(dirname)
