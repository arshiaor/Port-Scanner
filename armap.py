import sys, socket, time
from datetime import datetime
start_time=time.time()
target = ""
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Argument")
print("-" * 50)
print("starting scan on Target {} at {} ".format(target, str(datetime.now())))

try:
    for port in range(1, 20):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET: ip port , SOCK_STREAM : for tcp
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port)) #connect ex : if the host is up
        if result ==0:  #connection successful
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exitting the Program")
    sys.exit()
except socket.gaierror: #address related errors
    print("\n Hostname Could not be Resolved!")
    sys.exit()
except socket.error:
    print("\n Server Not responding!")
    sys.exit()
print("Runtime : {} seconds".format(time.time()-start_time))

