import web
import db

render = web.template.render('templates', base = 'base')

class Report:
    def GET(self, guid):
        report = db.get_report(guid)
        if report == None: return web.notfound()
        return render.report(report)
