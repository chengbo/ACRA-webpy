import web
import db
from models import report

render = web.template.render('templates', base = 'base')

class Report:
    def GET(self, guid):
        r = report.Report.get_report(guid)
        if r == None: return web.notfound()
        return render.report(r)
