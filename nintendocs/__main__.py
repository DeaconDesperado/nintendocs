from nintendocs import url_map
import tornado.web

application = tornado.web.Application(url_map,debug=True)
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()

