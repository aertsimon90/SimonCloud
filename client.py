import socket
class SimonCloud:
	def __init__(self, target="server", port=80):
		target = target+'.pythonanywhere.com'
		self.s = socket.socket()
		self.s.settimeout(20)
		self.s.connect((target, port))
		self.t = target;self.p = port
	def set(self, name, content): # Data Seting
		content = content.replace("\n", chr(1114111))
		p = f"GET / HTTP/1.1\r\nHost: {self.t}:{self.p}\r\nCommand: set {name} {content}\r\n\r\n".encode()
		self.s.sendall(p)
	def get(self, name): # Data Geting
		p = f"GET / HTTP/1.1\r\nHost: {self.t}:{self.p}\r\nCommand: get {name}\r\n\r\n".encode()
		self.s.sendall(p)
	def com(self, c): # Bash Command Runner
		p = f"GET / HTTP/1.1\r\nHost: {self.t}:{self.p}\r\nCommand: com {c}\r\n\r\n".encode()
		self.s.sendall(p)
	def recv(self):
		return self.s.recv(999999999).decode().split("\r\n\r\n")[1]