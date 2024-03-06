import json
import requests_toolbelt
from configparser import ConfigParser

def getJson(PATH):
    """ 
    Takes JSON file from PATH and converts on Dict obj
    args: PATH(str)
    returns: Dictionary Obj
    dependancy: import json 
    """ 
    with open(PATH) as payload_file:
        return json.load(payload_file)


def multiPartEnc(DICT):
    """ 
    Takes body dictionary and encodes as multipart obj
    args: DICT(Dictionary)
    returns: MultipartEncoder obj 
    dependacy: from requests_toolbelt import MultipartEncoder 
    """
    return requests_toolbelt.MultipartEncoder(fields=DICT)


def getIniConfig(PATH):
    """ 
    Takes .ini file path and returns config object
    args: PATH(str)
    returns: ConfigParser obj 
    dependacy: from configparser import ConfigParser 
    """
    configs=ConfigParser()
    configs.read(PATH)
    return configs



