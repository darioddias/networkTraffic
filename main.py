import threading
from capture.capture import start_capture
from processing.logstash_sender import start_logstash
from scripts.start_elasticsearch import start_elasticsearch
from scripts.start_kibana import start_kibana

def main():
    # Start Elasticsearch
    print("Starting Elasticsearch...")
    elasticsearch_thread = threading.Thread(target=start_elasticsearch)
    elasticsearch_thread.start()
    
    # Start Logstash
    print("Starting Logstash...")
    logstash_thread = threading.Thread(target=start_logstash)
    logstash_thread.start()
    
    # Start Kibana
    print("Starting Kibana...")
    kibana_thread = threading.Thread(target=start_kibana)
    kibana_thread.start()

    # Ensure Elasticsearch, Logstash, and Kibana are running before starting capture
    elasticsearch_thread.join()
    logstash_thread.join()
    kibana_thread.join()

    # Start capturing network traffic
    print("Starting network traffic capture...")
    capture_thread = threading.Thread(target=start_capture)
    capture_thread.start()

    # Join the capture thread to keep the main thread running
    capture_thread.join()

if __name__ == "__main__":
    main()
