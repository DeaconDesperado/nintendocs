import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, wrold!")

url_map = [
    (r"/", MainHandler),
]

if __name__ == "__main__":
    application = tornado.web.Application(url_map,debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
