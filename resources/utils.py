"""
methods:
    get_json
    multipath_encode
    get_ini_config
"""
import json
from configparser import ConfigParser

import requests_toolbelt

def get_json(path):
    """ 
    Takes JSON file from path and converts on Dict obj
    args: path(str)
    returns: Dictionary Obj
    dependancy: import json 
    """
    with open(path) as payload_file:
        return json.load(payload_file)


def multipart_encode(dict_obj):
    """ 
    Takes body dictionary and encodes as multipart obj
    args: dict_obj(Dictionary)
    returns: MultipartEncoder obj 
    dependacy: from requests_toolbelt import MultipartEncoder 
    """
    return requests_toolbelt.MultipartEncoder(fields=dict_obj)


def get_ini_config(path):
    """ 
    Takes .ini file path and returns config object
    args: path(str)
    returns: ConfigParser obj 
    dependacy: from configparser import ConfigParser 
    """
    configs=ConfigParser()
    configs.read(path)
    return configs
