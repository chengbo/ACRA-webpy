import web
import json

db = web.database(dbn='mysql', db = 'testdb', user = 'testuser', pw = '12345')

class FieldCount:
    _name = ""
    _count = 0

    @property
    def name(cls):
        return cls._name

    @property
    def count(cls):
        return cls._count

    @name.setter
    def name(cls, value):
        cls._name = value

    @count.setter
    def count(cls, value):
        cls._count = value

class FieldCountEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def get_field_count():
    distinct = db.query('SELECT DISTINCT ANDROID_VERSION FROM android_crash_reports')
    list1 = []
    for d in distinct:
        if d.ANDROID_VERSION == None: continue
        c = db.query('SELECT COUNT(*) AS count FROM android_crash_reports WHERE ANDROID_VERSION = $ver', vars = {'ver' : d.ANDROID_VERSION })[0].count
        v = FieldCount()
        v.name = d.ANDROID_VERSION
        v.count = c
        list1.append(v)
    return list1
