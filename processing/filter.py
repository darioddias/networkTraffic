from scapy.layers.inet import IP
from processing.logstash_sender import send_to_logstash

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        data = {
            "source_ip": ip_layer.src,
            "destination_ip": ip_layer.dst,
            "protocol": ip_layer.proto,
            "size": len(packet)
        }
        send_to_logstash(data)
