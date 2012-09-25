import web
import math
from models import report

render = web.template.render('templates', base = 'base')

class Reports:
    def GET(self):
        page_size = 10
        reports_count = report.Report.get_total_count()
        if reports_count == 0:
            return "No reports yet"
        pages_count = int(math.ceil(reports_count / (page_size * 1.0)))
        current_page = int(web.input(page=1).page)
        if current_page > pages_count:
            web.seeother('/reports')
        offset = (current_page - 1) * page_size
        reports = report.Report.get_reports(page_size, offset)
        return render.reports(reports, pages_count, current_page)
    def POST(self):
        i = web.input()
        report.Report.new_report(i)
        web.seeother('/reports')
