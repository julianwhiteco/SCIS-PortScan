import socket
import sys

print("Verbose Port Scanner by Suncoast Information Security")
domain = input("Enter domain to scan: ")
domain = domain.replace("http://", "")
domain = domain.replace("https://", "")


def scan_verbose():
    try:
        print("Please be patient, this recursive test can take some time.")

        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((domain, port))
            socket.setdefaulttimeout(10)
            if result == 0:
                print("Port " + "{} is open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("\n Keyboard abort pressed, process stopped.")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\n Server not responding.")
        sys.exit()


scan_verbose()
