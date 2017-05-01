#!/usr/bin/python

# Read config file
import yaml
from pymongo import MongoClient


class conn_db(object):
    ''' class to connect mongo '''
    netbackup_config = yaml.safe_load(open("C:\\Users\\arunrath\\PycharmProjects\\runbook_automation\\config.yaml"))

    def __init__(self, **kwargs):
        ''' constructor '''
        if kwargs is not None:
            #self.db_name = kwargs['db_name']
            self.client = MongoClient(host=self.netbackup_config['host'], \
                port=self.netbackup_config['port'])

    def get_dbh(self):
        ''' return the db handler '''
        dbh = self.client[self.netbackup_config['db_name']]
        return dbh

