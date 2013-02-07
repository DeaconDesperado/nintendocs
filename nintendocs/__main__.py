from nintendocs import application
import tornado.ioloop

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
