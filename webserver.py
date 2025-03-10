# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "local.nap.cid"
serverPort = 8080

class webserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path == "/":
		    self.path = '/index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "nap nap :)"
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost',192.168.100.5,7777,"local.nap.cid"), webserver)
httpd.serve_forever()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer, webserver)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
