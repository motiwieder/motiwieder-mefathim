import socket                   

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            
HOST = '127.0.0.1'     
PORT = 12345                   
BUFFER_SIZE = 1024

def conn():
	S.connect((HOST,PORT))
	S.send(b'helo')

def download():
	f = open('received_file', 'wb')
	print('file opened')
	
	while True:
		print('receiving data...')
		data = S.recv(BUFFER_SIZE)
		print('data=%s', (data))
		if not data:
			break
        
		f.write(data)

	f.close()
	print('Successfully get the file')
	S.close()
	print('connection closed')

def send_file():
	filename = '/home/adi/mefathim4/w.py'
	f = open(filename,'rb')
	while True:
		l = f.read(BUFFER_SIZE)
		while (l):
			S.send(l)
			l = f.read(BUFFER_SIZE)
		if not l:
			f.close()
			S.close()
			break

#def list_file():
def quit():
	s.send('QUIT')
	s.recv(BUFFER_SIZE)
	s.close()
	print('Server connection ended')
	return

if __name__ == "__main__":
	
	prompt = input('\n\nCall one of the following functions:\nCONN  to connect the server \nDOWNLOAD to download from the server\nsand file to sand file \nQUIT to ending')
	if prompt[:4].upper() == 'CONN':
		conn()
	elif prompt[:8].upper() == 'DOWNLOAD':
		download(prompt[5:])
	elif prompt[:9].upper() == 'SAND FILE':
		sand_file(prompt[5:])
	elif prompt[:4].upper() == 'QUIT':
		quit(prompt[5:])

