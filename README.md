# Python-ARP-Spoofing-with-Scapy-using-Subprocesses
(For educational purposes only)
This Python repository demonstrates ARP spoofing using the Scapy library, utilizing subprocesses for improved performance and flexibility. ARP spoofing is a technique used for intercepting network traffic by forging ARP (Address Resolution Protocol) messages. With this repository, you can easily execute ARP spoofing attacks, enabling network traffic interception and manipulation for security testing and educational purposes.

To run the script (on Linux distros), follow these steps:
  - make sure the machine is up to date
  - if using kali linux: no need to install scapy as it comes within the python package
  - make sure to set the appropriate network configurations for the script. 
  - Open a terminal window.
  - Navigate to the directory where the script is saved using the cd command.
  - Run the script using the python command followed by the script filename and the required arguments. i.e :
  - if your script is named arp_spoof.py and you want to spoof the ARP tables for a victim with IP address 192.168.1.200 and a host with IP address 192.168.1.1, with verbose output enabled, you would run:
     $python3 arp_spoof.py 192.168.1.200 192.168.1.1 --verbose

note: the script should run under root privileges using sudo -s as the super-user.  
This script was created for educational purpose only. use at your own risk.








