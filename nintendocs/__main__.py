from nintendocs import url_map
import tornado.web

application = tornado.web.Application(url_map,debug=True)
port = 8888
application.listen(port)
print "Running  server on port: " + str(port)
tornado.ioloop.IOLoop.instance().start()


