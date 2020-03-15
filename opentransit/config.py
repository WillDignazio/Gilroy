
import json
import os

class TransitServerConfigParser(object):
    def __init__(self):
        self.path = "%s/config/config.json" % (os.getcwd())
    
    def __init__(self, path):
        self.path = path
