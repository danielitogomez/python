import socket
from logo import logo

print(logo)

not_finish = False

while not not_finish:

    # input variables
    host = str(input("Enter some hostname or IP to scan\n"))
    port_range_min = int(input("Enter range start port to scan\n"))
    port_range_max = int(input("Enter range final port to scan\n"))
    ip = socket.gethostbyname(host)

    # scan function
    def scan_func():
        print("################################################################")
        print(f'### Scanning Ports for host {host} resolving ip {ip} ###')
        print("################################################################")
        print("")
        for port in range(port_range_min, port_range_max):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            output = sock.connect_ex((host, port))

            if output == 0:
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is not open')
            sock.close()


    scan_func()

    print("")

    should_continue = input("Do you want to continue doing scanning?\nType 'yes' or 'no'\n")
    if should_continue == "yes":
        not_finish = False
    elif should_continue == "no":
        not_finish = True
        print("Good bye!!!")
    else:
        print("Unknown input")
        exit(1)