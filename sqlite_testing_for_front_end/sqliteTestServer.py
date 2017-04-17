import sqlite3
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import logging
import signal
import time

is_closing = False


conn = sqlite3.connect('sqlitetest.db') #database file
conn.row_factory = sqlite3.Row #row object
c = conn.cursor()

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		c.execute(' SELECT * FROM EventLog ')
		l = c.fetchall()
		rows = [dict(i) for i in l]
		self.render("index.html", entries = rows)


class AddHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('add.html')

	def post(self):
		event = self.get_argument(name='event')
		veg = self.get_argument(name='veg')
		planter = int(self.get_argument(name='planter'))
		print type(planter)
		timelog = time.strftime('%Y-%m-%d %H:%M:%S')
		c.execute("INSERT INTO EventLog (Event, Vegetable, Timelog, Planter) VALUES (\'%s\',\'%s\',\'%s\',%d);" % (event, veg, timelog, planter))
		conn.commit()
		self.redirect("/add")

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
		(r'/(Tomatoes.png)', tornado.web.StaticFileHandler, {'path':'./'}),
		(r'/(custom.css)', tornado.web.StaticFileHandler, {'path': './'}),
		(r'/add', AddHandler)
	])


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

if __name__ == "__main__":
	tornado.options.parse_command_line()
	signal.signal(signal.SIGINT, signal_handler)

	app = make_app()
	app.listen(8888)

	tornado.ioloop.PeriodicCallback(exit, 100).start()

	tornado.ioloop.IOLoop.current().start()
