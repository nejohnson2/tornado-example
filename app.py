from tornado import websocket, web, ioloop
import json, os

class IndexHandler(web.RequestHandler):
	'''Handle requests on / '''
	@web.asynchronous
	def get(self, *args):
		self.write('<h1>Tornado Template</h1>')
		self.finish()

	@web.asynchronous
	def post(self, *args):
		data = json.loads(self.request.body)
		self.finish()

def main():
	app = web.Application(
		[
			(r'/', IndexHandler),
		],
		debug=True,
	)

	port = int(os.environ.get("PORT", 5000))
	print "Listening on port: %s"%(port)
	app.listen(port)
	ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()

	