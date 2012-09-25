import web

render = web.template.render('templates', base = 'base')

class Home:
    def GET(self):
        return render.home()
