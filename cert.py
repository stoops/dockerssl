import os, sys, subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

dnsr = "fossjon.com"

class serv(BaseHTTPRequestHandler):
	def do_GET(self):
		l = " &nbsp; "

		if self.path == "/ok":
			p = self.proc()
			(o, e) = p.communicate(timeout=180, input=b"\r\n")
			l += "<a href='/go'>Back</a>"

		elif self.path == "/go":
			p = self.proc()
			(o, e) = p.communicate(timeout=90)
			l += "<a href='/ok'>Verify</a>"

		else:
			o = b""
			l += "<a href='/go'>Ready</a>"

		l += " &nbsp; <a href='http://127.0.0.1:8000/etc/letsencrypt/archive/'>Download</a>"
		h = (o + b"\n\n" + l.encode())
		z = h.replace(b"\n", b"<br>")

		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(z)

	def proc(self):
		os.system("rm -frv /etc/letsencrypt/renewal/* /etc/letsencrypt/live/*")
		c = ("certbot certonly --manual --preferred-challenges=dns --email null@%s --agree-tos -d *.%s" % (dnsr, dnsr))
		p = subprocess.Popen(c.split(' '), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
		return p

webs = HTTPServer(("0.0.0.0", 8080), serv)
try:
	webs.serve_forever()
except:
	pass

webs.server_close()
