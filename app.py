#!/usr/bin/env python

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
        reports = db.get_reports()
        return render.index(reports)

class reports:
    def GET(self):
        return 'test'
    def POST(self):
        i = web.input()
        db.new_report(i)
        web.seeother('/')

class report:
    def GET(self, guid):
        return 'the guid is ' + guid

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
