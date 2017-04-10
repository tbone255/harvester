import sqlite3
import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

conn = sqlite3.connect('sqlitetest.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute(' SELECT * FROM EventLog ')
l = c.fetchall()
rows = [dict(i) for i in l]

print rows



class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html", entries = rows)

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
		(r'/(tomato.png)', tornado.web.StaticFileHandler, {'path':'./'}),
	])

app = make_app()
app.listen(8888)
tornado.ioloop.IOLoop.current().start()

conn.close()

