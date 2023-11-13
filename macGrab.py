import subprocess
import socket

#imprimir IP propia
ip = socket.gethostbyname(socket.gethostname())
print(ip)

#dividir ip en varios pedazos
routerIpArr = ip.split('.')
routerIpArr[3] = '0' #reemplazar por otra ip en la red

#reconstruir ip
routerIp = ''
for r in routerIpArr : routerIp += r+'.'
routerIp = routerIp[:-1]
print(routerIp)

#hacer ping a router (o a cualquier otra ip)
#command = 'ping ' + '-n ' + '1 ' + routerIp
command = ['ping','-n','1',routerIp]
res = subprocess.call(command)
print(res)

#comando mensajes
#msg * /server:<ip> "mensaje"