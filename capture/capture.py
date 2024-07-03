from scapy.all import sniff
from processing.filter import process_packet

def packet_callback(packet):
    process_packet(packet)

def start_capture():
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_capture()
