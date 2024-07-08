import socket
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="TCP Client Script", add_help=False)
parser.add_argument('-H', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
parser.add_argument("-h", "--target_host", required=True, help="The target host to connect to")
parser.add_argument("-p", "--target_port", type=int, default=80, help="The target port to connect to (default is 80)")

args = parser.parse_args()

target_host = args.target_host
target_port = args.target_port

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host).encode())

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
