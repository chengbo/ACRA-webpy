import web
import json
from models import fieldcount

class Statistics:
    def GET(self):
        fc = fieldcount.get_field_count()
        return json.dumps(fc, cls = fieldcount.FieldCountEncoder)
