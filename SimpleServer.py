import ScreenHelpers
import web #pip3 install web.py

render = web.template.render('templates/')
helper = ScreenHelpers.screenHelper()
urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class index:

    def GET(self, name):
        helper.TakeScreenshotOfDesktop()
        return render.index(name)


if __name__ == "__main__":
    app.run()
