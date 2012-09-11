import web

db = web.database(dbn='mysql', db = 'testdb', user = 'testuser', pw = '12345')

def get_reports():
    return db.select('android_crash_reports')

def new_report(data):
    db.insert('android_crash_reports', REPORT_ID = data.REPORT_ID, APP_VERSION = data.myAppVerCode, APP_VERSION_NAME = data.myAppVerName, ANDROID_VERSION = data.ANDROID_VERSION, PHONE_MODEL = data.PHONE_MODEL, PHONE_BRAND = data.BRAND, PRODUCT = data.PRODUCT, USER_CRASH_DATE = data.USER_CRASH_DATE, PACKAGE_NAME = data.PACKAGE_NAME, STACK_TRACE = data.STACK_TRACE)
