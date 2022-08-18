import socket
import threading
import time

# input variables
host = str(input("Enter some hostname or IP to scan\n"))

# define scan_ports function
def scan_ports(port):
    try:

        host_ip = socket.gethostbyname(host)

        # create instance of socket
        output_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connecting host ip address and port
        output_socket.connect((host_ip, port))
        try:
            banner = output_socket.recv(1024).decode()
            print("Port {} is open with banner {}".format(port, banner))

        except:
            print("Port {} is open ".format(port))

    except:
        pass


start_time = time.time()

# scan all ports
for i in range(0, 64120):
    thread = threading.Thread(target=scan_ports, args=[i])
    thread.start()

end_time = time.time()
print("To scan all ports took {} seconds".format(end_time - start_time))