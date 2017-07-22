import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import logging
import signal
import time


is_closing = False
app_path = '/Users/eli/Documents/harvester/harvester/harvester_fe/harvester-app/'

#looks for a signal
def signal_handler(signum, frame):
	global is_closing
	logging.info('exiting, please wait')
	is_closing = True

#if is_closing is true then it closes tornado
def exit():
	global is_closing
	if(is_closing):
		tornado.ioloop.IOLoop.instance().stop()
		conn.close()
		logging.info('exited')


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(app_path + 'dist/index.html')

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
		(r'/favicon.ico', tornado.web.StaticFileHandler, {'path':app_path + 'dist/favicon.ico'}),
		(r'/inline.31a4c59f35c74ed381bc.bundle.js', tornado.web.StaticFileHandler, {'path':app_path + 'dist/inline.31a4c59f35c74ed381bc.bundle.js'}),
		(r'/main.bc5a7e610b2682bd43f7.bundle.js', tornado.web.StaticFileHandler, {'path':app_path + 'main.bc5a7e610b2682bd43f7.bundle.js'}),
		(r'/polyfills.ab8304790a25edec7f7d.bundle.js', tornado.web.StaticFileHandler, {'path':app_path + 'dist/polyfills.ab8304790a25edec7f7d.bundle.js'}),
		(r'/styles.d41d8cd98f00b204e980.bundle.css', tornado.web.StaticFileHandler, {'path':app_path + 'dist/styles.d41d8cd98f00b204e980.bundle.css'}),
		(r'/vendor.a3600978aa648c90bd39.bundle.js', tornado.web.StaticFileHandler, {'path':app_path + 'dist/vendor.a3600978aa648c90bd39.bundle.js'})
		#(r'/(Tomatoes.png)', tornado.web.StaticFileHandler, {'path':'./'}),
		#(r'/(custom.css)', tornado.web.StaticFileHandler, {'path': './'}),
		#(r'/add', AddHandler)
	])

if __name__ == "__main__":
	tornado.options.parse_command_line()
	signal.signal(signal.SIGINT, signal_handler)

	app = make_app()
	app.listen(8888)

	tornado.ioloop.PeriodicCallback(exit, 100).start()

	tornado.ioloop.IOLoop.current().start()
