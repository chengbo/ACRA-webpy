import web
import json

db = web.database(dbn='mysql', db = 'testdb', user = 'testuser', pw = '12345')

def get_report(guid):
    try:
        return db.select('android_crash_reports', where= 'REPORT_ID = $guid', vars = locals())[0]
    except IndexError:
        return None

def get_reports(limit, offset):
    return db.select('android_crash_reports', offset = offset, limit = limit)

def get_reports_count():
    return db.query('SELECT COUNT(*) AS count FROM android_crash_reports')[0].count

def new_report(data):
    db.insert('android_crash_reports', REPORT_ID = data.REPORT_ID, APP_VERSION = data.myAppVerCode, APP_VERSION_NAME = data.myAppVerName, ANDROID_VERSION = data.ANDROID_VERSION, PHONE_MODEL = data.PHONE_MODEL, PHONE_BRAND = data.BRAND, PRODUCT = data.PRODUCT, USER_CRASH_DATE = data.USER_CRASH_DATE, PACKAGE_NAME = data.PACKAGE_NAME, STACK_TRACE = data.STACK_TRACE)

class Version:
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

class VersionEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def get_field_count():
    distinct = db.query('SELECT DISTINCT ANDROID_VERSION FROM android_crash_reports')
    dict1 = {}
    list1 = []
    for d in distinct:
        if d.ANDROID_VERSION == None: continue
        c = db.query('SELECT COUNT(*) AS count FROM android_crash_reports WHERE ANDROID_VERSION = $ver', vars = {'ver' : d.ANDROID_VERSION })[0].count
        dict1[d.ANDROID_VERSION] = c
        v = Version()
        v.name = d.ANDROID_VERSION
        v.count = c
        list1.append(v)
    print list1
    return list1
