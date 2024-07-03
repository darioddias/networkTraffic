import os
import subprocess

def start_logstash():
    logstash_config_path = "/path/to/config/logstash.conf"  # Update with actual path
    subprocess.run(["logstash", "-f", logstash_config_path])
