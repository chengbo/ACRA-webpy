#!/usr/bin/env python

import math
import web
import db
import json

urls = (
    '/', 'index',
    '/reports', 'reports',
    '/reports/([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})', 'report',
    '/statistics', 'statistics'
)

render = web.template.render('templates', base='base')

class index:
    def GET(self):
        return render.index()

class reports:
    def GET(self):
        page_size = 10
        reports_count = db.get_reports_count()
        if reports_count == 0:
            return "No reports yet"
        pages_count = int(math.ceil(reports_count / (page_size * 1.0)))
        current_page = int(web.input(page=1).page)
        if current_page > pages_count:
            web.seeother('/reports')
        offset = (current_page - 1) * page_size
        reports = db.get_reports(page_size, offset)
        return render.reports(reports, pages_count, current_page)
    def POST(self):
        i = web.input()
        db.new_report(i)
        web.seeother('/reports')

class report:
    def GET(self, guid):
        report = db.get_report(guid)
        if report == None: return web.notfound()
        return render.report(report)

class statistics:
    def GET(self):
        dd = db.get_field_count()
        return json.dumps(dd, cls=db.VersionEncoder)

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
