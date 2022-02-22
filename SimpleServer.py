import ScreenHelpers
import web #pip3 install web.py


import web
render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)

class index:

    global helper
    helper = ScreenHelpers.screenHelper()

    def GET(self, name):
        helper.TakescreenshotOfDesktop()
        return render.index(name)




if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
