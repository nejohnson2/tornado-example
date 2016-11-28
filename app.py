from tornado import websocket, web, ioloop
import json, os

cl = []

class IndexHandler(web.RequestHandler):
	'''Handle requests on / '''
	def get(self):
		self.render("index.html")

class WebSocketHandler(websocket.WebSocketHandler):
	# Not sure if this is necessary
	def check_origin(self, origin):
		return True

	def open(self):
		print "Client connected"    	
		if self not in cl:
			cl.append(self)

	def on_close(self):
		if self in cl:
			cl.remove(self)

	def on_message(self, message):
		print "Client received message: %s" %(message)

class ApiHandler(web.RequestHandler):
	@web.asynchronous
	def get(self, *args):
		"""GET: <url>:5000/api?temp=X&hum=Y"""
		self.finish()

		try:
			# parse URL for parameters (not sure why this is in GET request and not POST)
			data = {"temp": self.get_argument("temp"), 
					"hum": self.get_argument("hum"),
					}

			data = json.dumps(data)

			# send data to all clients
			for c in cl:
				c.write_message(data)		

		except:
			pass

	@web.asynchronous
	def post(self, *args):
		"""receive data from JSON POST request"""
		data = json.loads(self.request.body)
		self.finish()

def main():
	settings = {
		"template_path": os.path.join(os.path.dirname(__file__), "templates"),
		"static_path": os.path.join(os.path.dirname(__file__), "static"),
		"debug" : True
	}

	app = web.Application(
		[
			(r'/', IndexHandler),
			(r'/ws', WebSocketHandler),
			(r'/api', ApiHandler),
		], **settings
	)

	port = int(os.environ.get("PORT", 5000))
	print "Listening on port: %s"%(port)
	app.listen(port)
	ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()

	