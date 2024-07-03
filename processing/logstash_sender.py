import socket
import json
import time

def start_logstash(logstash_host='localhost', logstash_port=5044, data=None):
    """
    Starts or interacts with a Logstash instance by sending data.

    Args:
    - logstash_host (str): Hostname or IP address of the Logstash server.
    - logstash_port (int): Port number on which Logstash is listening.
    - data (dict): Data to send to Logstash (default: None).

    Example:
    - Establishes a socket connection to Logstash.
    - Sends data to Logstash as JSON.
    - Handles exceptions if the connection or data transmission fails.
    """
    if not data:
        data = {"message": "Hello, Logstash!", "source": "network_traffic_analyzer"}

    try:
        # Create a socket connection to Logstash
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((logstash_host, logstash_port))

        # Send data to Logstash as JSON
        message = json.dumps(data)
        sock.sendall(message.encode('utf-8'))
        sock.send(b'\n')  # Required for Logstash JSON Lines input

        # Close the socket connection
        sock.close()

        print(f"Successfully sent data to Logstash at {logstash_host}:{logstash_port}")

    except ConnectionRefusedError:
        print(f"Connection to Logstash at {logstash_host}:{logstash_port} refused.")
    except Exception as e:
        print(f"Failed to send data to Logstash: {str(e)}")

# Example usage:
if __name__ == "__main__":
    start_logstash()
