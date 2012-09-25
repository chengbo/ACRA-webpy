#!/usr/bin/env python

import web
import controllers

urls = (
    '/', 'controllers.home.Home',
    '/reports', 'controllers.reports.Reports',
    '/reports/([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})', 'controllers.report.Report',
    '/statistics', 'controllers.statistics.Statistics'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
