import web
import db
import json

class Statistics:
    def GET(self):
        dd = db.get_field_count()
        return json.dumps(dd, cls = db.VersionEncoder)
