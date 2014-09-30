import SimpleHTTPServer
import SocketServer
import BaseHTTPServer
import urlparse
from os import curdir, sep
HOST_NAME = "10.0.0.2"
PORT_NUMBER = 8000
class Webserver(BaseHTTPServer.BaseHTTPRequestHandler):
	PORT = 8000
	HOST = "10.0.0.2"
	def connect_to_fileserver(self, HOST, PORT):
		handler_class = SimpleHTTPServer.SimpleHTTPRequestHandler
		httpd = SocketServer.TCPServer((HOST, PORT), handler_class)
		print "serving at port", PORT
		httpd.serve_forever()
	
	def connect_to_base(self,HOST, PORT):
		handler_class = BaseHTTPServer.BaseHTTPRequestHandler
		server_class = BaseHTTPServer.HTTPServer
		server_address = (HOST, PORT)
		httpd = server_class(server_address, handler_class)
		try:
			httpd.serve_forever()
		except KeyboardInterrupt:
			pass
		httpd.server_close()
		print "Server Stops - %s:%s" % (HOST, PORT)
			
	def do_GET(self):
		try:
			if self.path == "/":														
				self.path = "index.html"
			if self.path.endswith(".html"):
				contentype = "text/html"
			elif self.path.endswith(".txt"):
				contentype ="text/plain" 
			parsed_path = urlparse.urlparse(self.path)
			try:
				params = dict([p.split('=') for p in parsed_path[4].split('&')])
			except:
				params = {}
			f = open(curdir + sep + self.path)
			self.send_response(200)
			self.send_header("Content-type", contentype)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		except:
			self.send_error(404, 'File Not Found: %s' %self.path)
		#self.wfile.write("<html><head><title>Title goes here.</title></head>")
		#self.wfile.write("<body><p>This is a test.</p>")
		# If someone went to "http://something.somewhere.net/foo/bar/",
		# then s.path equals "/foo/bar/".
		#self.wfile.write("<p>You accessed path: %s</p>" % self.path)
		#self.wfile.write("<p>params %s</p>" %params)
		#self.wfile.write("</body></html>")
	
if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), Webserver)
	print "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)