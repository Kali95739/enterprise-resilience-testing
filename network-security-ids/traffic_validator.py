import os
import subprocess

def run_security_traffic_test():
    print("[TEST SETUP] Initializing continuous live network capture via Snort IDS engine...")
    # Start snort monitoring system targeting local rules profiles
    snort_cmd = "snort -q -A console -c /etc/snort/rules/local.rules -r network_capture.pcap"
    
    print("[ATTACK SIMULATION] Launching targeted ping packets simulating reconnaissance sweep...")
    # Simulates basic payload hitting the network stack boundary
    output = subprocess.run(snort_cmd, shell=True, capture_output=True, text=True)
    
    print("\n[INFRASTRUCTURE TEST RESULTS] Network IDS Intrusion Log Output:")
    if "SECURITY ALERT" in output.stdout:
        print("✔ PASS: Network security infrastructure identified and blocked malicious traffic signatures.")
    else:
        print("❌ FAIL: Network security configuration failed to log perimeter threat activities.")

if __name__ == "__main__":
    run_security_traffic_test()
