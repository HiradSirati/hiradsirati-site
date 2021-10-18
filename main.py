import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
  server.bind(("https://hiradsirati-site.herokuapp.com/", 8000))
  server.listen()
  server_is_on = True
  while server_is_on:
    connection, address = server.accept()
