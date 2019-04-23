import socket

UDP_IP = "192.168.50.255"
UDP_PORT = 1111
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

MESSAGE = "SSI:STRT:RUN1\0"
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
print("Recording message Sent")
