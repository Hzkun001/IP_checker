import socket
import requests

def print_logo(self):
        colors = [36, 32, 34, 35, 31, 37]

        x = """


                    White HaT Hackers
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗    ██╗██████╗
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    ██║██╔══██╗
██║     ███████║█████╗  ██║     █████╔╝     ██║██████╔╝
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗     ██║██╔═══╝
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    ██║██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝╚═╝
                    Hz-exploit

     Note! : We don't Accept any responsibility for any illegal usage.     >
    """
print('{x}')
print('Tools by Hz_Exploit')
hostname = input('Enter a domain name: ')
ip_address = socket.gethostbyname(hostname)

print(f'Domain Name: {hostname}')
print(f'IP Address: {ip_address}')
