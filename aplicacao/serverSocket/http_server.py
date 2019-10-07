import socket
import sys

def getMimetype(path):
  mimetype = 'Content-Type: '
  ext = path.split('.')[-1]

  if ext == 'txt':
    mimetype += 'text/plain'
  elif ext in ['jpg', 'jpeg']:
    mimetype += 'image/jpeg'
  elif ext == 'png':
    mimetype += 'image/png'
  elif ext == 'html':
    mimetype += 'text/html'
  else: 
    return None

  mimetype += '\r\n'
  return mimetype


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 4000))
server_socket.listen(1)

print('Server is listening on port {}'.format(4000))

while(True):
  connection, addr = server_socket.accept()
  message = connection.recv(1024).decode('utf-8')
  messageParts = message.split(' ')

  print('user {} was connected.'.format(addr))

  try:
    method = messageParts[0]
    path = messageParts[1]
    httpVersion = messageParts[2].split('\r\n')[0] 

    if path == '/':
        path += 'index.html'
    

    fileName = path.split('/')[-1]
    file = open( '.' + path, 'rb')
    responseBody  = file.read()
    file.close()

    header = '{} 200 OK\r\n'.format(httpVersion)

    mimetype = getMimetype(path)
    if mimetype:
        header += mimetype
    else:
        header += 'Content-Disposition: form-data; name="files"; filename="{}"\r\n'.format(fileName)

    print('method {} returns {}'.format(method, path))

  except:
    header = '{} 404 Not Found\n\n'.format(httpVersion)
    page404 = open( './404.html', 'rb')
    responseBody = page404.read()
    print('method {} file "{}" not found.'.format(method, fileName))
      
  response = header.encode('utf-8')
  response += '\r\n'.encode('utf-8')
  response += responseBody
  response += '\r\n'.encode('utf-8')

  connection.send(response)
  connection.close()
