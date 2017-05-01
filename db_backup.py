from conn_db import conn_db
from pprint import  pprint

from collections import namedtuple
from bson.objectid import ObjectId
import sys

obj = conn_db()

class Mininons_Db(object):
    """ model class for the collection nbackup_request """

    dbh = obj.get_dbh()

    def __init__(self):
        """ constructor """
        self._user = None
        self._port = None
        self._instance = None
        self._hostname = None
        self._location_or_dc = None
        self._os = None

    def insert(self):
        """ to insert a record """
        return self.add()

    def fetchport(self):
        if self._port is not None:
            port = self.dbh.nbackup_request.find({"port":self._port})
            pprint(self.dbh.nbackup_request.find({"port":self._port}))
            return port
        else:
            return None


    def save(self):
        """ to insert a record """
        return self.add()

    def add(self):
        """ to insert a record """

        # rec_dict = dict()

        # for attr in dir(self):
        #    if not (attr.startswith('__') or attr.startswith('_')) and not callable(getattr(self,attr)):
        #        rec_dict[attr] = eval('self.' + attr)

        # ret = self.dbh.nbackup_request.insert(rec_dict)
        pprint(self._user)
        record = {
            "user": self._user,
            "port": self._port,
            "instance": self._instance,
            "hostname": self._hostname,
            "location_or_dc": self._location_or_dc,
            "os": self._os
        }
        
        pprint(record)
        rec = self.dbh.nbackup_request.insert_one(record)
        return str(rec.inserted_id)

    def search(self):
        """ to search record(s) """

        rec_dict = dict()

        for attr in dir(self):
            if not (attr.startswith('__') or attr.startswith('_')) and not callable(getattr(self, attr)):
                if getattr(self, attr):
                    if attr == 'id':
                        rec_dict['_id'] = getattr(self, attr)
                    else:
                        rec_dict[attr] = getattr(self, attr)

        if 'id' in rec_dict:
            del rec_dict['id']
        # ret = self.dbh.nbackup_request.find(rec_dict, {'_id':0})
        ret = self.dbh.nbackup_request.find(rec_dict)

        return ret




def delete(self):
    """ to delete a record """
    if self._hostname is not None:
        ret = self.dbh.nbackup_request.delete_many({"hostname": self._hostname})
        return ret.deleted_count
    else:
        return None


def remove(self):
    """ to delete a record """
    return self.delete()


def user():
    def fget(self):
        """ getter """
        return self._user

    def fset(self, value):
        self._user = value

    def fdel(self):
        del self._user

    return locals()
user = property(**user())

def port():
    def fget(self):
        """ getter """
        return self._port

    def fset(self, value):
        self._port = value

    def fdel(self):
        del self._port

    return locals()

port = property(**port())

def instance():
    def fget(self):
        """ getter """
        return self._instance

    def fset(self, value):
        self._instance = value

    def fdel(self):
        del self._instance

    return locals()
instance = property(**instance())

def hostname():
    def fget(self):
        """ getter """
        return self._hostname

    def fset(self, value):
        self._hostname = value

    def fdel(self):
        del self._hostname

    return locals()
hostname = property(**hostname())


def location_or_dc():
    def fget(self):
        """ getter """
        return self._location_or_dc

    def fset(self, value):
        self._location_or_dc = value

    def fdel(self):
        del self._location_or_dc

    return locals()
location_or_dc = property(**location_or_dc())


def os():
    def fget(self):
        """ getter """
        return self._os

    def fset(self, value):
        self._os = value


    def fdel(self):
        del self._os

    return locals()
os = property(**os())
























































































































