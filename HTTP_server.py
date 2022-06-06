# Modifying some code from opensource
# Python based HTTP server
# credit to the unknown owner


import BaseHTTPServer 
 
class Handle(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/my/'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head><title>Server Testing</title></head><body>Eggs</body></html>')
        else:
            # Use Default from here and modify
            return
 
httpd = BaseHTTPServer.HTTPServer(("", 8000), Handle)
httpd.serve_forever()
