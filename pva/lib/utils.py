try:
   import cPickle as pickle
except:
   import pickle
import os
import glob
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
    try:
        with open(filename, 'wb') as f:
            pickle.dump(object, f)
            return True
    except Exception:
        return False


def load_dumped_object(filename):
    """
    Load, deserialize and returns object from file
    :param filename: full path to file
    :return Object:
    """
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except Exception:
        return None


def create_directory(dirname):
    """
    Create directory
    :param dirname: full path to directory
    """
    try:
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return True
    except Exception:
        return False


def get_recent_file(dirname, ext=None):
    """
    Get most recent file in a directory
    :param dirname: directory path
    :param ext: file extension
    :return String: filepath
    """
    if ext:
        files_pattern = dirname+'*.'+ext
    else:
        files_pattern = dirname+'*'
    return max(glob.iglob(files_pattern), key=os.path.getctime)
