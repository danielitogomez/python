import socket
import threading
import time

# input variables
host = str(input("Enter some hostname or IP to scan\n"))
start_port = int(input(("Enter start port\n")))
end_port = int(input("Enter end port\n"))


def scan_port(port):
    try:
        host_ip = socket.gethostbyname(host)
        status = False

        # create instance of socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        # connecting the host ip address and port
        s.connect((host_ip, port))
        try:
            banner = s.recv(1024).decode()
            print("port {} is open with banner {}".format(port, banner))

        except:
            print("port {} is open ".format(port))

    except:
        pass


start_time = time.time()

for i in range(start_port, end_port):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()

end_time = time.time()
print("To scan all ports using sockets lib it took {} seconds".format(end_time - start_time))