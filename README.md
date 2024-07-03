# Network Traffic Analyzer

Network Traffic Analyzer is a tool designed to monitor and analyze network traffic for patterns, bandwidth usage, and potential bottlenecks. It implements features like real-time traffic visualization and alert systems.

## Features

- Capture network traffic using Scapy
- Process and filter captured packets
- Send processed data to Logstash for further analysis
- Real-time traffic visualization using D3.js
- Alert system for potential network issues

## Technologies Used

- Python
- Scapy
- Logstash (part of the ELK stack)
- D3.js for visualization

## Project Structure

```plaintext
network_traffic_analyzer/
│
├── capture/
│   └── capture.py
│
├── processing/
│   ├── filter.py
│   └── logstash_sender.py
│
├── scripts/
│   ├── start_elasticsearch.py
│   └── start_kibana.py
│
├── .venv/
│   └── ...
│
├── main.py
├── README.md
└── requirements.txt


Getting Started

Prerequisites

- Python 3.10 or higher
- Scapy
- Logstash
- Elasticsearch
- Kibana
- Node.js and npm (for D3.js visualization)

Installation

- Clone the repository:
  - git clone https://github.com/yourusername/network_traffic_analyzer.git
  - cd network_traffic_analyzer

- Set up a virtual environment and install dependencies:
  - python -m venv .venv
  - source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
  - pip install -r requirements.txt

- Ensure Logstash, Elasticsearch, and Kibana are installed and running

Configuration

- Configure Logstash to listen on port 5044 for incoming data. Example Logstash configuration (logstash.conf):
  -   input {
    tcp {
      port => 5044
      codec => json_lines
    }
  }

  output {
    elasticsearch {
      hosts => ["localhost:9200"]
      index => "network-traffic-%{+YYYY.MM.dd}"
    }    
    stdout { codec => rubydebug }
  }

Usage

- Start capturing network traffic:
  - python main.py

- Visualize the captured data using D3.js:
  - cd visualization
  - npm install
  - npm start

- Access Kibana to view and analyze the processed data

Files Overview

- capture/capture.py
  - Handles capturing network traffic using Scapy.

- processing/filter.py
  - Processes and filters captured packets.

- processing/logstash_sender.py
  - Sends processed data to Logstash.

- scripts/start_elasticsearch.py
  - Starts the Elasticsearch service.

- scripts/start_kibana.py
  - Starts the Kibana service.

- main.py
  - Main entry point for the application. Initializes and runs the network traffic analyzer.

Contributing

- Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or enhancements.

License

- This project is licensed under the MIT License - see the LICENSE file for details.
