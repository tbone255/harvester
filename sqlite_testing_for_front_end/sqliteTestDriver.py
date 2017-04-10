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




class MainHandler(tornado.web.RequestHandler):
	def get(self):
		c.execute( 'SELECT * FROM EventLog' )
		l = c.fetchall()
		rows = [dict(i) for i in l]
		self.render("index.html", title = "HarvesterNew", entries = rows)

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
		])

app = make_app()
app.listen(8888)
tornado.ioloop.IOLoop.current().start()

conn.close()

