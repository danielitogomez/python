import os

file = open("hosts.txt","r")

for server_name in file:
    server_state = os.system('ping -c 1 ' + server_name )
    if server_state == 0:
        print(server_name +"===== Server is UP=====")
        f = open("hosts_output_up.txt", "a")
        f.write(str(server_name) + ' is up ' + '\n')
        f.close()
        print("\n")
    else:
        print("=====Server is DOWN====")
        f = open("hosts_output_down.txt", "a")
        f.write(str(server_name) + ' is down or unreachable ' + '\n')
        f.close()
        print("\n")