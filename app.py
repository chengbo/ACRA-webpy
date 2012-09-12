#!/usr/bin/env python

import math
import web
import db

urls = (
    '/', 'index',
    '/reports', 'reports',
    '/reports/([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})', 'report'
)

render = web.template.render('templates', base='base')

class index:
    def GET(self):
        return render.index()

class reports:
    def GET(self):
        page_size = 10
        reports_count = db.get_reports_count()
        pages_count = math.ceil(reports_count / (page_size * 1.0))
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

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
