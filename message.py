import subprocess
import socket

#imprimir IP propia
ip = socket.gethostbyname(socket.gethostname())
print(ip)

command = 'msg */server:'+ ip
#command = ['msg */server:',ip,' "',input(">> "),'"']
subprocess.call(command)
